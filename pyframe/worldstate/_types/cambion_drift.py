import datetime
from dataclasses import dataclass
from typing import Literal, TypedDict

from typing_extensions import Self

from .base_objects import WorldstateObject, Record


class _CambionDriftRecord(Record, TypedDict):
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
    def _from_response(cls: 'CambionDrift', response: _CambionDriftRecord) -> Self:
        return cls(
            activation=datetime.datetime.fromisoformat(response["activation"]),
            expiry=datetime.datetime.fromisoformat(response["expiry"]),
            active=response["active"],
            state=response["state"],
            time_left=response["timeLeft"],
        )
