import logging

# Put in code before starting to log, afterwards is it of no use
#logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(name)s:%(message)s")
#logging.basicConfig(format="{levelname}:{name}:{message}", style="{")
# filemode a --> append
logging.basicConfig(
    level=logging.DEBUG,
    filename="logger-3.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M %Z",
)

logging.debug("Some debug log record")
logging.info("Some info log record")
logging.warning("Some warning log record")
logging.error("Some error log record")
logging.critical("Some critical log record")

donuts = 5
guests = 0
try:
    donuts_per_guest = donuts / guests
except ZeroDivisionError:
    logging.error("DonutCalculationError", exc_info=True)

try:
    donuts_per_guest = donuts / guests
except ZeroDivisionError:
    logging.exception("DonutCalculationError")


