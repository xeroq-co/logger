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
    def __init__(self, fmt=None, datefmt=None, session=""):
        super().__init__(fmt, datefmt)
        self.session = session

    def formatTime(self, record, datefmt=None):
        est = pytz.timezone("US/Eastern")
        dt = datetime.fromtimestamp(record.created, est)
        return dt.strftime(datefmt or "%Y-%m-%d %H:%M:%S")

    def format(self, record):
        color = LOG_COLORS.get(record.levelname, "")
        message = super().format(record)
        session_str = f"[{self.session}] " if self.session else ""
        return f"{color}{session_str}{message}{RESET_COLOR}"

    def set_session(self, session):
        self.session = session

class StaticLogger:
    _logger = None
    _formatter = None

    @staticmethod
    def get_logger(name=None, level=logging.DEBUG):
        if StaticLogger._logger is None:
            logger = logging.getLogger(name)
            logger.setLevel(level)
            if not logger.handlers:
                handler = logging.StreamHandler()
                StaticLogger._formatter = ESTFormatter(
                    "%(asctime)s - %(levelname)s - %(pathname)s:%(lineno)d - %(message)s"
                )
                handler.setFormatter(StaticLogger._formatter)
                logger.addHandler(handler)
            StaticLogger._logger = logger
        return StaticLogger._logger

    @staticmethod
    def setSession(session):
        if StaticLogger._formatter is not None:
            StaticLogger._formatter.set_session(session)

# Example usage
if __name__ == "__main__":
    logger = StaticLogger.get_logger()
    logger.debug("This is a debug message.\nThis is a debug message.")
    logger.info("This is an info message.")
    StaticLogger.setSession("session-123")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")
