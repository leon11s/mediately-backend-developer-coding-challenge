from flightsparser import LOG_LEVEL, SERVICE_NAME

from flightsparser.scrapers import DepartureScraper, WeatherScraper
import logging


logger = logging.getLogger(f"{SERVICE_NAME}")

if LOG_LEVEL == "debug":
    logger.setLevel(logging.DEBUG)
elif LOG_LEVEL == "info":
    logger.setLevel(logging.INFO)
elif LOG_LEVEL == "warning":
    logger.setLevel(logging.WARNING)
elif LOG_LEVEL == "error":
    logger.setLevel(logging.ERROR)
else:
    logger.setLevel(logging.DEBUG)

# Create handlers
cmd_handler = logging.StreamHandler()

# Create formatters and add it to handlers
log_format = logging.Formatter("[%(asctime)s] - %(name)s - %(levelname)s - %(message)s")
cmd_handler.setFormatter(log_format)

# Add handlers to the logger
logger.addHandler(cmd_handler)


logger.info(f"Starting {SERVICE_NAME}...")

# temperature_scraper = WeatherScraper()
# departure_scraper = DepartureScraper(download_automatic=True)
# # with open("tests/data/departures.html") as f:
# #     departure_scraper.page_raw_html = f.read()

# # print(departure_scraper.page_raw_html[:5000])
# deps = departure_scraper.extract()
# for dep in deps:
#     print(dep)
