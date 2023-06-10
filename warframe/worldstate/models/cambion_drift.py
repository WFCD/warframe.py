from datetime import datetime
from typing import Literal, Optional

from ..common import SingleQueryModel

__all__ = ["CambionDrift"]


class CambionDrift(SingleQueryModel):
    __endpoint__ = "/cambionCycle"

    # required
    expiry: datetime
    "The time the Cycle ends"

    activation: datetime
    "The time the new rotation of the cycle started"

    state: Literal["vome", "fass"]
    'The state of the Cambion Drift. ("vome" or "fass")'

    # optional
    time_left: Optional[str] = None
