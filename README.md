# Mediately backend developer coding challenge

## Usage
### Command line interface
Before running the commands you should:
- Instaling web driver
    - `sudo apt-get install firefox-geckodriver`
- Create virtual env: `python -m venv .venv` (first time)
- Activate virtual env: `source .venv/bin/activate`
- Install requirements: `pip install -r requirements_dev.txt`
- Run Redis and PostgreSQL localy if needed:
    - `sudo docker-compose up -d`
- Run tests: `pytest -vv`
- Config: `./flightsparser/config.cfg`

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

### Production version
To install Docker and docker-compose run (on Ubuntu):
    - `./docker_setup.sh`

The container periodically run the scraping pipeline that outputs the weather at destinations of flights leaving Vienna airport. The env variables can be edited in the `docker-compose.prod.yml` file:
- `PARSE_INTERVAL_SECONDS`: Seconds between to runs of the scraper.
- `CACHE_TYPE`: The type of cache to use by the scraper. 
    - `redis`: The scraped data is stored in Redis cache. Redis instance configuration variables: **REDIS_HOST**, **REDIS_PORT**, **EXPIRATION_TIME_SECONDS** (expiration time of the data in the cache).
    - `local`: The scraped data is stored locally on disk.
    - `none`: Cache not used. 
- `SAVE_RESULTS_TO_DB`: If **True** data are stored in database. The database is configured with  **DATABASE_CONN_URI**, **NOTE_TABLE_NAME** variables.

- Run: `sudo docker-compose --file=docker-compose.prod.yml up -d --build`
- Stop: `sudo docker-compose --file=docker-compose.prod.yml down -v`
