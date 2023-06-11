from datetime import datetime
from typing import Literal, Optional

from ..common import SingleQueryModel, TimedEvent

__all__ = ["Cetus"]


class Cetus(SingleQueryModel, TimedEvent):
    __endpoint__ = "/cetusCycle"

    # required
    is_day: bool
    "Whether it is currently day on the Plains of Eidolon"

    @property
    def state(self):
        """
        The state of the Plains of Eidolon ("day" or "night")
        """
        return "day" if self.is_day else "night"
