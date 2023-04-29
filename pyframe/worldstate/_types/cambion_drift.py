import datetime
from dataclasses import dataclass
from typing import Literal

from typing_extensions import Self

from .base import WorldstateObject, Record


class _CambionDriftRecord(Record):
    expiry: str
    activation: str
    state: Literal["vome", "fass"]
    active: Literal["vome", "fass"]
    timeLeft: str


@dataclass(frozen=True, order=True)
class CambionDrift(WorldstateObject):
    expiry: datetime.datetime
    activation: datetime.datetime
    state: Literal["vome", "fass"]
    active: Literal["vome", "fass"]
    time_left: str

    @classmethod
    def _from_response(cls: "CambionDrift", response: _CambionDriftRecord) -> Self:
        return cls(
            activation=datetime.datetime.fromisoformat(response["activation"]),
            expiry=datetime.datetime.fromisoformat(response["expiry"]),
            active=response.get("active"),
            state=response.get("state"),
            time_left=response.get("timeLeft"),
        )
