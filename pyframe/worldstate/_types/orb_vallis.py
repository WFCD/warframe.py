import datetime
from dataclasses import dataclass
from typing import Literal, Optional, TypedDict

from typing_extensions import Self

from .base import WorldstateObject, Record

__all__ = [
    "OrbVallis"
]

class _OrbVallisRecord(Record):
    # required
    expiry: str
    timeLeft: str
    isWarm: bool

    # optional
    activation: Optional[str]
    state: Optional[str]
    shortString: Optional[str]


@dataclass(frozen=True, order=True)
class OrbVallis(WorldstateObject):
    # required
    expiry: datetime.datetime
    time_left: str
    is_warm: bool

    # optional
    activation: Optional[datetime.datetime]
    state: Optional[Literal["warm", "cold"]]

    @classmethod
    def _from_response(cls: "OrbVallis", response: _OrbVallisRecord) -> Self:
        return cls(
            activation=datetime.datetime.fromisoformat(response.get("activation").strip("Z"))
            if "activation" in response
            else None,
            expiry=datetime.datetime.fromisoformat(response.get("expiry").strip("Z")),
            time_left=response.get("timeLeft"),
            is_warm=response.get("isWarm"),
            state=response.get("state"),
        )
