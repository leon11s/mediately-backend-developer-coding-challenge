import logging

from flightsparser import SERVICE_NAME, SAVE_RESULTS_TO_DB
from flightsparser.db import NotesTable
from flightsparser.scrapers import DepartureData, DepartureScraper

_logger = logging.getLogger(f"{SERVICE_NAME}.{__name__}")

if SAVE_RESULTS_TO_DB:
    notes_table = NotesTable()


def create_note(departure: DepartureData):
    if departure.temperature:
        if departure.temperature > 10:
            feeling = "warm"
        else:
            feeling = "cold"
        return f"The weather in {departure.city} is {feeling}. "
    else:
        _logger.warning(f"Temperature missing for {departure}")
        return None


def create_notes(cache="local", key=None, save_to_db=False):
    if key:
        _logger.info(f"Extrating data from cache with key: {key}")
        scraper = DepartureScraper(cache=cache)
        departures = scraper.extract_from_cache(key=key)
    else:
        _logger.debug("Extrating departures data...")
        scraper = DepartureScraper(cache=cache)
        departures = scraper.extract()

    for departure in departures:
        departure.note = create_note(departure)
        _logger.debug(f"{departure}  -> NOTE: {departure.note}")
        if save_to_db:
            _logger.info("Saving data to DB.")
            notes_table.insert(departure)
