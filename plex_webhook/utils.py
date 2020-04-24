from plexapi.server import PlexServer
import os
import logging
import time
import datetime
from pylogrus import PyLogrus, TextFormatter, JsonFormatter

def get_logger():
    try:
        logging.setLoggerClass(PyLogrus)
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        formatter = TextFormatter(datefmt='Z', colorize=True)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        return logger
    except Exception as e:
        raise("Error getting logger: ", e)

logger = get_logger()

def processEvent(payload):
    if not payload:
        logger.error("Empty payload. Early return.")
        return
    plex = PlexServer(os.environ["PLEXAPI_AUTH_SERVER_BASEURL"], os.environ["PLEXAPI_AUTH_SERVER_TOKEN"])
    event_type = payload.get('event')
    if not event_type or event_type == '':
        logger.error("No event type")
        return
    logger.info(f'Processing {event_type} event.')
    # Do your thing
    