import logging
from logging import Logger, getLogger


def get_logger(name: str) -> Logger:
    logger = getLogger(name)
    logger.setLevel(logging.DEBUG)
    return logger
