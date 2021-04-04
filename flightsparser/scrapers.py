import datetime
import logging
from typing import List, Union

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from flightsparser import (
    SERVICE_NAME,
    VIENNA_AIRPORT_URL,
    WEATHER_API_KEY,
    WEATHER_API_URL,
)
from flightsparser.cache import LocalCache, RedisCache

_logger = logging.getLogger(f"{SERVICE_NAME}.{__name__}")


class DepartureData:
    def __init__(
        self,
        timestamp: datetime.datetime = None,
        city: str = None,
        temperature: int = None,
    ) -> None:
        self.timestamp = timestamp
        self.city = city
        self.temperature = temperature
        self.note = None

    def __str__(self) -> str:
        return f"Departure to {self.city} at {self.timestamp}. Temp: {self.temperature}"


class WeatherScraper:
    def __init__(self) -> None:
        self.api_key = WEATHER_API_KEY
        self.url = WEATHER_API_URL

    def get_temperature(self, city_name: str) -> Union[int, None]:
        city_name = self.__fix_city_name(city_name)
        full_url = f"{self.url}?q={city_name.lower()}&appid={self.api_key}&units=metric"
        temperature = requests.get(full_url).json().get("main", {}).get("temp")
        if temperature:
            return int(temperature)

    def __fix_city_name(self, city_name: str):
        if city_name == "Paris CDG":
            return "Paris"
        elif city_name == "Addis Ab.":
            return "Addis Abeba"
        elif city_name == "Seoul ICN":
            return "Seoul"
        elif city_name == "Rom FCO":
            return "Rome"
        elif city_name == "London LHR":
            return "London"
        elif city_name == "Moskau DME":
            return "Moscow"
        elif city_name == "Kiew":
            return "Kyiv"
        else:
            return city_name


class DepartureScraper:
    def __init__(self, cache="local") -> None:
        self.url = VIENNA_AIRPORT_URL
        self.weather_scraper = WeatherScraper()
        self.cache = None
        if cache == "local":
            self.cache = LocalCache()
        elif cache == "redis":
            self.cache = RedisCache()

    def extract(self) -> List[DepartureData]:
        self.download_page()
        departures = self.__parse_departures()
        if self.cache:
            cache_key = self.__get_cache_key()
            self.cache.add_element(key=cache_key, data=departures)
            print(f"Departures saved to cache: {cache_key}")
        return departures

    def extract_from_cache(self, key: str):
        if self.cache:
            return self.cache.get_element(key)
        print("Cache option not enabled!")

    def download_page(self) -> None:
        try:
            browser = webdriver.Firefox(
                firefox_profile=self.__get_webdriver_profile(),
                firefox_options=self.__get_firefox_options(),
            )
            browser.get(self.url)
            self.page_raw_html = browser.page_source
            _logger.info(f"Extracting: {browser.title}")
        except BaseException as err:
            _logger.error(f"Error: {err}")
        finally:
            browser.quit()

    def __get_webdriver_profile(self):
        profile = webdriver.FirefoxProfile()
        return profile

    def __get_firefox_options(self):
        opts = webdriver.FirefoxOptions()
        opts.add_argument("--headless")
        return opts

    def __parse_departures(self):
        departures_parsed = []
        soup = BeautifulSoup(self.page_raw_html, "html.parser")
        departures_raw = soup.find("div", class_="fd-detail-rows")
        departures = departures_raw.find_all("div", class_="detail-table__row")
        date = departures[0].text.strip()

        for departure in departures[1:]:
            time = departure.find_all("div", class_="detail-table__cell")[
                0
            ].text.strip()
            city_raw = departure.find_all("div", class_="detail-table__cell")[1]
            city = city_raw.find("span", class_="visible-xs").text.strip()
            temperature = self.weather_scraper.get_temperature(city)
            timestamp = self.__parse_timestamp(date, time)
            departures_parsed.append(DepartureData(timestamp, city, temperature))
        return departures_parsed

    def __parse_timestamp(self, date: str, time: str) -> datetime.datetime:
        timestamp_joined = f"{date} {time}"
        return datetime.datetime.strptime(timestamp_joined, "%d.%m.%Y %H:%M")

    def __get_cache_key(self) -> str:
        return datetime.datetime.now().strftime("%Y_%m_%dT%H_%M_%S")
