"""Central logging configuration for workflow tools."""

from __future__ import annotations

import logging
import sys
from pathlib import Path
from typing import Optional
import logging
from contextlib import contextmanager
from typing import Optional, Iterator
from gh_paths import GH_LOGS_DIR


def _configure_root_logger() -> None:
    """Configure root logger with stdout/stderr handlers once."""
    root_logger = get_root_logger()
    if root_logger.handlers:
        return
    root_logger.setLevel(logging.INFO)
    formatter = get_standard_logger_formatter()
    log_dir = GH_LOGS_DIR
    print(f"Logging to: {log_dir}")
    if log_dir:
        log_path = Path(log_dir)
        log_path.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_path / "workflow.log")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)
    else:
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setLevel(logging.INFO)
        stdout_handler.setFormatter(formatter)
        root_logger.addHandler(stdout_handler)

        stderr_handler = logging.StreamHandler(sys.stderr)
        stderr_handler.setLevel(logging.WARNING)
        stderr_handler.setFormatter(formatter)
        root_logger.addHandler(stderr_handler)


def get_root_logger() -> logging.Logger:
    """Get the root logger."""
    return logging.getLogger()


def get_standard_logger_formatter() -> logging.Formatter:
    """Return the default logger formatter.

    The formatter outputs log records in the format:
    YYYY-MM-DD-HH:MM:SS.mmm LEVEL MESSAGE

    Milliseconds are included after the seconds field for higher
    precision. Example:

        2025-09-12-14:35:42.123 INFO Processing started
    """
    return logging.Formatter(
        fmt="%(asctime)s.%(msecs)03d %(levelname)s %(message)s",
        datefmt="%Y-%m-%d-%H:%M:%S",
    )


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """Return a module-specific logger with default configuration."""
    print("\n" + name + " called get_logger")
    _configure_root_logger()
    return logging.getLogger(name)


@contextmanager
def make_specific_logger(
    name: Optional[str], log_path: str, rootless: bool = False
) -> Iterator[logging.Logger]:
    """Context manager that yields a logger with a file handler attached.

    Args:
        name: Logger name (None for root logger).
        log_path: Path to the log file.
        rootless: If True, root logger and specific logger are logging separately;
                  Otherwise (default) the handler is attached to both the logger
                  and the root logger.

    Yields:
        logging.Logger: Configured logger instance.
    """
    print("\n" + name + " called make_specific_logger")

    handler = logging.FileHandler(log_path, encoding="utf-8")
    handler.setFormatter(get_standard_logger_formatter())

    logger = logging.getLogger(name)
    if not rootless:
        root_logger = get_root_logger()

    logger.setLevel(logging.INFO)

    logger.addHandler(handler)
    if not rootless:
        root_logger.addHandler(handler)
        root_logger.info(
            "================================START===================================="
        )
        root_logger.info("log:  %s", name)
        root_logger.info("path: %s", log_path)
        root_logger.info(
            "------------------------------------------------------------------------"
        )

    try:
        yield logger
    finally:
        logger.removeHandler(handler)
        if not rootless:
            root_logger.info(
                "================================END====================================="
            )
            root_logger.removeHandler(handler)
        handler.close()
