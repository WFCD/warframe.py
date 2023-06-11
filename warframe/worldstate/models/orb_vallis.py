from datetime import datetime
from typing import Literal, Optional

from ..common import SingleQueryModel, TimedEvent

__all__ = ["OrbVallis"]


class OrbVallis(SingleQueryModel, TimedEvent):
    __endpoint__ = "/vallisCycle"

    # required
    is_warm: bool
    "Whether it is currently warm"

    @property
    def state(self) -> Literal["warm", "cold"]:
        """
        The state of the Plains of Eidolon ("warm" or "cold")
        """
        return "warm" if self.is_warm else "cold"
