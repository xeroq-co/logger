import logging
import os
import pytz
from datetime import datetime

# Set the timezone to EST
EST = pytz.timezone('America/New_York')

# ANSI escape sequences for colorizing log messages
class LogColors:
    DEBUG = "\033[94m"  # Blue
    INFO = "\033[92m"   # Green
    WARNING = "\033[93m" # Yellow
    ERROR = "\033[91m"  # Red
    CRITICAL = "\033[95m" # Magenta
    RESET = "\033[0m"    # Reset to default

class CustomFormatter(logging.Formatter):
    def format(self, record):
        # Get the current time in EST
        record.timestamp = datetime.now(EST).strftime('%Y-%m-%d %H:%M:%S')
        # Add full path and line number to the log record
        record.fullpath = os.path.abspath(record.pathname)
        record.lineno = record.lineno
        
        # Determine color based on log level
        if record.levelno == logging.DEBUG:
            color = LogColors.DEBUG
        elif record.levelno == logging.INFO:
            color = LogColors.INFO
        elif record.levelno == logging.WARNING:
            color = LogColors.WARNING
        elif record.levelno == logging.ERROR:
            color = LogColors.ERROR
        elif record.levelno == logging.CRITICAL:
            color = LogColors.CRITICAL
        else:
            color = LogColors.RESET
        
        # Format the log message with color
        log_message = f"{color}{record.timestamp} - {record.levelname} - {record.fullpath}:{record.lineno} - {record.msg}{LogColors.RESET}"
        return log_message

def setup_logger(name='custom_logger', level=logging.DEBUG):
    """Sets up the custom logger."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create a console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # Create a formatter and set it for the handler
    formatter = CustomFormatter()
    ch.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(ch)

    return logger

# Example usage
if __name__ == "__main__":
    logger = setup_logger()
    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")
