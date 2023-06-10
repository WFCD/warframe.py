from datetime import datetime
from typing import Literal, Optional

from ..common import SingleQueryModel

__all__ = ["Cetus"]


class Cetus(SingleQueryModel):
    __endpoint__ = "/cetusCycle"

    # required
    expiry: datetime
    "The time the Cycle ends"

    is_day: bool
    "Whether it is currently day on the Plains of Eidolon"

    time_left: str
    "Short formatted time string on how much time is left on the current cycle"

    # optional
    activation: Optional[datetime] = None
    "The time the new rotation of the cycle started"

    start_string: Optional[str] = None
    "Short-time-formatted duration string representing the start of the alert"

    short_string: Optional[str] = None
    "Short-time-formatted duration string representing the start of the alert"

    @property
    def state(self):
        """
        The state of the Plains of Eidolon ("day" or "night")
        """
        return "day" if self.is_day else "night"
