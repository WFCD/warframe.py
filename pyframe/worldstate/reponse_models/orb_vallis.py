from datetime import datetime
from dataclasses import dataclass
from typing import Literal, Optional

from ..common import WorldstateObject

__all__ = ["OrbVallis"]


@dataclass(frozen=True, order=True)
class OrbVallis(WorldstateObject):
    # required
    expiry: datetime
    timeLeft: str
    isWarm: bool

    # optional
    activation: Optional[datetime]
    state: Optional[Literal["warm", "cold"]]
