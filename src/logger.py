import logging
import inspect
import sys

from loguru import logger

logger.remove(0)

logger.add(sys.stdout, level="INFO", diagnose=False, backtrace=False, enqueue=True)
logger.add(
    "logs/error.log",
    level="ERROR",
    filter=lambda record: record["level"].name == "ERROR",
    backtrace=True,
    diagnose=False,
    enqueue=True,
)
logger.add(
    "logs/info.log",
    level="INFO",
    rotation="10 MB",
    filter=lambda record: record["level"].name == "INFO",
    enqueue=True,
)


class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        level: str | int
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = inspect.currentframe(), 0
        while frame and (depth == 0 or frame.f_code.co_filename == logging.__file__):
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )
