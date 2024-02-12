import logging
log_level = {
    "DEBUG" : logging.DEBUG,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
    "INFO": logging.INFO,
}

def get_log_level(level) :
    return log_level.get(level, logging.ERROR)