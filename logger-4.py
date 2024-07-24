import logging

logger = logging.getLogger(__name__)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("logger-4.log", mode="a", encoding="utf-8")

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.warning(logger.handlers)
logger.warning("Look at my logger")