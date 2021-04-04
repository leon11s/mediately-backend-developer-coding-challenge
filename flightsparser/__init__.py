import os
import pathlib
from configparser import ConfigParser as _ConfigParser
from distutils.util import strtobool

import importlib_resources as _resources

_cfg = _ConfigParser()

with _resources.path("flightsparser", "config.cfg") as _path:
    _cfg.read(str(_path))


# --- GENERAL --- #
LOG_LEVEL = os.getenv("LOG_LEVEL", str(_cfg.get("GENERAL", "LOG_LEVEL")))
SERVICE_NAME = os.getenv("SERVICE_NAME", str(_cfg.get("GENERAL", "SERVICE_NAME")))
CACHE_PATH = f"{pathlib.Path(__file__).parent.absolute()}/local_cache.pkl"
PARSE_INTERVAL_SECONDS = int(
    os.getenv(
        "PARSE_INTERVAL_SECONDS", str(_cfg.get("GENERAL", "PARSE_INTERVAL_SECONDS"))
    )
)
CACHE_TYPE = os.getenv("CACHE_TYPE", str(_cfg.get("GENERAL", "CACHE_TYPE")))
SAVE_RESULTS_TO_DB = bool(
    strtobool(
        os.getenv("SAVE_RESULTS_TO_DB", str(_cfg.get("GENERAL", "SAVE_RESULTS_TO_DB")))
    )
)


# --- SCRAPERS --- #
VIENNA_AIRPORT_URL = os.getenv(
    "VIENNA_AIRPORT_URL", str(_cfg.get("SCRAPERS", "VIENNA_AIRPORT_URL"))
)

WEATHER_API_KEY = os.getenv(
    "WEATHER_API_KEY", str(_cfg.get("SCRAPERS", "WEATHER_API_KEY"))
)

WEATHER_API_URL = os.getenv(
    "WEATHER_API_URL", str(_cfg.get("SCRAPERS", "WEATHER_API_URL"))
)


# --- DATABASE --- #
DATABASE_CONN_URI = os.getenv(
    "DATABASE_CONN_URI", str(_cfg.get("DATABASE", "DATABASE_CONN_URI"))
)
NOTE_TABLE_NAME = os.getenv(
    "NOTE_TABLE_NAME", str(_cfg.get("DATABASE", "NOTE_TABLE_NAME"))
)


# --- REDIS --- #
REDIS_HOST = os.getenv("REDIS_HOST", str(_cfg.get("REDIS", "REDIS_HOST")))
REDIS_PORT = int(os.getenv("REDIS_PORT", str(_cfg.get("REDIS", "REDIS_PORT"))))
EXPIRATION_TIME_SECONDS = int(
    os.getenv(
        "EXPIRATION_TIME_SECONDS", str(_cfg.get("REDIS", "EXPIRATION_TIME_SECONDS"))
    )
)
