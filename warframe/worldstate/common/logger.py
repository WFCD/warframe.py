from __future__ import annotations

import logging
import os
import sys
from typing import Any, NewType

ColorStr = NewType("ColorStr", str)


class Color:
    grey = ColorStr("\x1b[38;5;240m")  # Grey text
    yellow = ColorStr("\x1b[33;1m")  # Yellow text (bold)
    red = ColorStr("\x1b[31m")  # Red text
    bold_red = ColorStr("\x1b[31;1m")  # Bold Red text
    blue = ColorStr("\x1b[34m")  # Blue text
    green = ColorStr("\x1b[32m")  # Green text
    magenta = ColorStr("\x1b[35m")  # Magenta text
    cyan = ColorStr("\x1b[36m")  # Cyan text
    white = ColorStr("\x1b[1;37m")  # Bold white text
    black = ColorStr("\x1b[30;1m")  # Bright Black
    bold = ColorStr("\x1b[40;1m")

    # Background colors
    bg_black = ColorStr("\x1b[40m")  # Black background
    bg_white = ColorStr("\x1b[47m")  # White background
    bg_blue = ColorStr("\x1b[44m")  # Blue background
    bg_green = ColorStr("\x1b[42m")  # Green background

    reset = ColorStr("\x1b[0m")  # Reset to default


def c(text: object, color: ColorStr) -> str:
    """
    Color a text. Rather short func name for more readable calls within stuff like f-strings.

    Parameters
    ----------
    text : str
        The text to color.
    color : ColorStr
        The color to use.

    Returns
    -------
    str
        The colored string.
    """
    return f"{color}{text}{Color.reset}"


class DefaultWorldstateFormatter(logging.Formatter):
    LEVEL_COLOURS = [
        (logging.DEBUG, Color.white),
        (logging.INFO, Color.blue),
        (logging.WARNING, Color.yellow),
        (logging.ERROR, Color.red),
        (logging.CRITICAL, Color.red),
    ]

    FORMATS = {
        level: logging.Formatter(
            f"[{c('%(asctime)s', Color.grey)} {c('%(levelname)-8s', color)} {c('%(name)-40s', Color.magenta)}] %(message)s",
            "%Y-%m-%d %H:%M:%S",
        )
        for level, color in LEVEL_COLOURS
    }

    def format(self, record):
        formatter = self.FORMATS.get(record.levelno)
        if formatter is None:
            formatter = self.FORMATS[logging.DEBUG]

        # Override the traceback to always print in red
        if record.exc_info:
            text = formatter.formatException(record.exc_info)
            record.exc_text = c(text, Color.red)

        output = formatter.format(record)

        # Remove the cache layer
        record.exc_text = None
        return output


def _is_docker() -> bool:
    path = "/proc/self/cgroup"
    return os.path.exists("/.dockerenv") or (
        os.path.isfile(path) and any("docker" in line for line in open(path))
    )


def stream_has_color_support(stream: Any) -> bool:
    is_a_tty = hasattr(stream, "isatty") and stream.isatty()

    # Pycharm and Vscode support colour in their inbuilt editors
    if "PYCHARM_HOSTED" in os.environ or os.environ.get("TERM_PROGRAM") == "vscode":
        return is_a_tty

    if sys.platform != "win32":
        # Docker does not consistently have a tty attached to it
        return is_a_tty or _is_docker()

    # ANSICON checks for things like ConEmu
    # WT_SESSION checks if this is Windows Terminal
    return is_a_tty and ("ANSICON" in os.environ or "WT_SESSION" in os.environ)
