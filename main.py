import logging
import time
import traceback

from flightsparser import (
    CACHE_TYPE,
    LOG_LEVEL,
    PARSE_INTERVAL_SECONDS,
    SAVE_RESULTS_TO_DB,
    SERVICE_NAME,
)
from flightsparser.note import create_notes

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


def main() -> None:
    cache = CACHE_TYPE
    if cache == "none":
        cache = None
    while True:
        create_notes(cache=cache, save_to_db=SAVE_RESULTS_TO_DB)
        time.sleep(PARSE_INTERVAL_SECONDS)


if __name__ == "__main__":
    try:
        logger.info(f"Starting {SERVICE_NAME}...")
        main()
    except BaseException as exc:
        traceback_str = "".join(traceback.format_tb(exc.__traceback__))
        logger.error(f"Unexpected error: {exc}!\n {traceback_str}")
    finally:
        logger.info(f"Exiting {SERVICE_NAME}...")
