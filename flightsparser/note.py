from flightsparser.scrapers import DepartureScraper, DepartureData


def create_note(departure: DepartureData):
    if departure.temperature > 10:
        return "vroce"
    else:
        return "mrzlo"


def create_notes(cache="local", key=None, save_to_db=False):
    if key:
        scraper = DepartureScraper(cache=cache)
        departures = scraper.extract_from_cache(key=key)
    else:
        scraper = DepartureScraper(cache=cache)
        departures = scraper.extract()
    for departure in departures:
        note = create_note(departure)
        print(f"{departure}  -> NOTE: {note}")
        if save_to_db:
            pass
