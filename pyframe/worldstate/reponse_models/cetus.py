import datetime
from dataclasses import dataclass
from typing import Literal, Optional

from ..common import WorldstateObject

__all__ = ["Cetus"]


@dataclass(frozen=True, order=True)
class Cetus(WorldstateObject):
    # required
    expiry: datetime.datetime
    isDay: bool
    time_left: str

    # optional
    activation: Optional[datetime.datetime]
    startString: Optional[str]
    active: Optional[bool]
    state: Optional[Literal["day", "night"]]
    shortString: Optional[str]
