# 


## Commands

- Instaling web driver
`sudo apt-get install firefox-geckodriver`

## Development 
- Create virtual env: `python -m venv .venv` (first time)
- Activate virtual env: `source .venv/bin/activate`
- Install requirements: `pip install -r requirements_dev.txt`

## Usage

### Command line interface

- List cached departures:
    - `python -m flightsparser --list-cached-departures`
- Extract departures data and save data to cache:
    - `python -m flightsparser --extract-departures`
- Extract departures data (no cache):
    - `python -m flightsparser --extract-departures-no-cache`
- Create notes (no cache):
    - `python -m flightsparser --create-notes`
- Create notes from cache:
    - `python -m flightsparser --create-notes-from-cache --cache-key <CACHE_KEY>`