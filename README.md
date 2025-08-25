# Bittensor Logger Module

A custom Python logging module with colorized output and EST timestamps.  
Displays full file path and line number for each log message.

## Features

- Color-coded log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- EST timezone timestamps
- Full file path and line number in logs

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Import and set up the logger in your Python code:

```python
from hlogger import setup_logger

logger = setup_logger()
logger.info("This is an info message.")
```

## Example Output

```
2025-08-25 12:34:56 - INFO - D:\logger\hlogger.py:49 - This is an info message.
```

## Requirements

See `requirements.txt` for dependencies.

## License

MIT