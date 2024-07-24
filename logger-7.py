import logging

logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("logger-7.log", mode="a", encoding="utf-8")
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# You define the lowest allowed log level on the logger itself.
# Handlers can’t show logs lower than the defined log level of the logger they’re connected to.
logger.setLevel("DEBUG")
console_handler.setLevel("DEBUG")
file_handler.setLevel("INFO")

formatter = logging.Formatter(
"{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M %Z"
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.debug("Some debug log record")
logger.info("Some info log record")
logger.warning("Some warning log record")
logger.error("Some error log record")
logger.critical("Some critical log record")