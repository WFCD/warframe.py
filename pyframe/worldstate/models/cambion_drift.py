from datetime import datetime
from typing import Literal, Optional

from ..common import SupportsSingle, WorldstateObject

__all__ = ["CambionDrift"]


class CambionDrift(WorldstateObject, SupportsSingle):
    # required
    expiry: datetime
    activation: datetime
    state: Literal["vome", "fass"]

    # optional
    time_left: Optional[str] = None
