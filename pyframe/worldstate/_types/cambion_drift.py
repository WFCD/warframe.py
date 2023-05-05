import datetime
from dataclasses import dataclass
from typing import Literal, Optional

from typing_extensions import Self

from .base import WorldstateObject, Record

__all__ = [
    "CambionDrift"   
]

class _CambionDriftRecord(Record):
    # required
    expiry: str
    activation: str
    state: Literal["vome", "fass"]

    # optional
    timeLeft: Optional[str]


@dataclass(frozen=True, order=True)
class CambionDrift(WorldstateObject):
    # required
    expiry: datetime.datetime
    activation: datetime.datetime
    state: Literal["vome", "fass"]

    # optional
    time_left: Optional[str]

    @classmethod
    def _from_response(cls: "CambionDrift", response: _CambionDriftRecord) -> Self:
        return cls(
            activation=datetime.datetime.fromisoformat(response.get("activation").strip("Z")),
            expiry=datetime.datetime.fromisoformat(response.get("expiry").strip("Z")),
            state=response.get("state"),
            time_left=response.get("timeLeft"),
        )
