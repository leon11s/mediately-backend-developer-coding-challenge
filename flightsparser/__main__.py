# clear cache files
# list caches

import argparse

from flightsparser import CACHE_TYPE, SAVE_RESULTS_TO_DB
from flightsparser.cache import LocalCache
from flightsparser.note import create_notes
from flightsparser.scrapers import DepartureScraper


def main():
    parser = argparse.ArgumentParser(
        description="Command line interface for flightsparser."
    )
    parser.add_argument("--list-cached-departures", action="store_true")
    parser.add_argument("--extract-departures", action="store_true")
    parser.add_argument("--extract-departures-no-cache", action="store_true")
    parser.add_argument("--create-notes", action="store_true")
    parser.add_argument("--create-notes-from-cache", action="store_true")
    parser.add_argument("--cache-key", action="store")
    args = parser.parse_args()

    if args.list_cached_departures:
        cache = LocalCache()
        elements = cache.get_cache_elements()
        print("CACHED ITEMS: ")
        for index, el in enumerate(elements, 1):
            print(f"--> {index}) {el}")
    elif args.extract_departures:
        scraper = DepartureScraper(cache=CACHE_TYPE)
        data = scraper.extract()
        print("Extracting departures...")
        for departure in data:
            print(departure)
    elif args.extract_departures_no_cache:
        scraper = DepartureScraper(cache=None)
        data = scraper.extract()
        print("Extracting departures no cache...")
        for departure in data:
            print(departure)
    elif args.create_notes:
        print("Creating notes...")
        create_notes(cache=CACHE_TYPE, save_to_db=SAVE_RESULTS_TO_DB)
    elif args.create_notes_from_cache:
        if args.cache_key:
            print("Creating notes from cache...")
            create_notes(
                cache="local", key=args.cache_key, save_to_db=SAVE_RESULTS_TO_DB
            )
        else:
            print("Please provide a cache key.")


if __name__ == "__main__":
    main()
