from datetime import datetime
from typing import Literal, Optional

from ..common import SingleQueryModel

__all__ = ["CambionDrift"]


class CambionDrift(SingleQueryModel):
    __endpoint__ = "/cambionCycle"

    # required
    expiry: datetime
    activation: datetime
    state: Literal["vome", "fass"]

    # optional
    time_left: Optional[str] = None
