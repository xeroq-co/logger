import logging
import pytz
from datetime import datetime

LOG_COLORS = {
    "DEBUG": "\033[36m",     # Cyan
    "INFO": "\033[32m",      # Green
    "WARNING": "\033[33m",   # Yellow
    "ERROR": "\033[31m",     # Red
    "CRITICAL": "\033[41m",  # Red background
}
RESET_COLOR = "\033[0m"

class ESTFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        est = pytz.timezone("US/Eastern")
        dt = datetime.fromtimestamp(record.created, est)
        return dt.strftime(datefmt or "%Y-%m-%d %H:%M:%S")

    def format(self, record):
        color = LOG_COLORS.get(record.levelname, "")
        message = super().format(record)
        return f"{color}{message}{RESET_COLOR}"

def setup_logger(name=None, level=logging.DEBUG):  # <-- Changed default to DEBUG
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = ESTFormatter(
            "%(asctime)s - %(levelname)s - %(pathname)s:%(lineno)d - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

# Example usage
if __name__ == "__main__":
    logger = setup_logger()
    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")
