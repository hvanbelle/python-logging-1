import logging

# Put in code before starting to log, afterwards is it of no use
#logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(name)s:%(message)s")
#logging.basicConfig(format="{levelname}:{name}:{message}", style="{")
# filemode a --> append
logging.basicConfig(
    level=logging.DEBUG,
    filename="logger-2.log",
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

name = "Samara"
logging.debug(f"{name=}")

# Self-Documenting Expressions
variable = "Some mysterious value"
print(f"{variable = }")
print(f"{variable=}")
print(f"{variable= }")
print(f"{variable =}")
