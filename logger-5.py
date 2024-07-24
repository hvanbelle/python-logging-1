import logging

logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("logger-5.log", mode="a", encoding="utf-8")
logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.setLevel("DEBUG")

formatter = logging.Formatter(
"{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M %Z",
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.warning(logger.handlers)
logger.warning("Look at my logger")

logger.debug("Some debug log record")
logger.info("Some info log record")
logger.warning("Some warning log record")
logger.error("Some error log record")
logger.critical("Some critical log record")