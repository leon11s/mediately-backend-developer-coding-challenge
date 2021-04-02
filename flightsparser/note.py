from flightsparser.scrapers import DepartureScraper, DepartureData


def create_note(departure: DepartureData):
    if departure.temperature > 10:
        return "vroce"
    else:
        return "mrzlo"


def create_notes(cache=None, key=None, save_to_db=False):
    if cache == "local":
        if not key:
            print("You should provide a cache key when using cache mode.")
            return
        scraper = DepartureScraper()
        departures = scraper.extract_from_cache(key=key, cache="local")
    elif cache == "redis":
        pass
    else:
        scraper = DepartureScraper()
        departures = scraper.extract()
    for departure in departures:
        note = create_note(departure)
        print(f"{departure}  -> NOTE: {note}")
        if save_to_db:
            pass
