import logging
from typing import Any, TypeAlias

from .common.logger import DefaultWorldstateFormatter, stream_has_color_support

MISSING: TypeAlias = Any


def _get_lib_name() -> str:
    if "." in __name__:
        return __name__.split(".")[-1]
    else:
        return __name__


def setup_logging(
    *,
    handler: logging.Handler = MISSING,
    formatter: logging.Formatter = MISSING,
    level: int = MISSING,
    root: bool = MISSING,
) -> None:
    """
    Helper function for setting up logging.

    Parameters
    ----------
    handler : logging.Handler, optional
        The handler to use, by default MISSING
    formatter : logging.Formatter, optional
        The formatter to use, by default MISSING
    level : int, optional
        The level for the logging (e.g. logging.DEBUG), by default MISSING
    root : bool, optional
        Register the logger as root, by default MISSING
    """
    if level is MISSING:
        level = logging.INFO

    if handler is MISSING:
        handler = logging.StreamHandler()

    if formatter is MISSING:
        # fmt: off
        if isinstance(handler, logging.StreamHandler) and stream_has_color_support(handler.stream):
            formatter = DefaultWorldstateFormatter()
        else:
            dt_fmt = "%Y-%m-%d %H:%M:%S"
            formatter = logging.Formatter(
                "[{asctime}] [{levelname:<8}] {name}: {message}", dt_fmt, style="{"
            )
        # fmt: on

    if root:
        logger = logging.getLogger()
    else:
        lib = _get_lib_name()
        logger = logging.getLogger(lib)

    handler.setFormatter(formatter)
    logger.setLevel(level)
    logger.addHandler(handler)
