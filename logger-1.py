import logging

# Put in code before starting to log, afterwards is it of no use
# basisConfig --> only for root-logger
#logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(name)s:%(message)s")
#logging.basicConfig(format="{levelname}:{name}:{message}", style="{")
logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M %Z",
)

logging.debug("Some debug log record")
logging.info("Some info log record")
logging.warning("Some warning log record")
logging.error("Some error log record")
logging.critical("Some critical log record")