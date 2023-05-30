from dataclasses import dataclass
from datetime import datetime
from typing import Literal, Optional

from ..common import WorldstateObject

__all__ = ["CambionDrift"]


@dataclass(frozen=True, order=True)
class CambionDrift(WorldstateObject):
    # required
    expiry: datetime
    activation: datetime
    state: Literal["vome", "fass"]

    # optional
    timeLeft: Optional[str]
