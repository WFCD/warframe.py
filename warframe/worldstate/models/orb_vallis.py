from datetime import datetime
from typing import Literal, Optional

from ..common import SingleQueryModel

__all__ = ["OrbVallis"]


class OrbVallis(SingleQueryModel):
    __endpoint__ = "/vallisCycle"

    # required
    expiry: datetime
    "The time the Cycle ends"

    time_left: str
    "Short formatted time string on how much time is left on the current cycle"

    is_warm: bool
    "Whether it is currently warm"

    # optional
    activation: Optional[datetime] = None
    "The time the new rotation of the cycle started"

    state: Optional[Literal["warm", "cold"]] = None
    "The state of the vallis (warm/cold)"
