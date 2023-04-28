import datetime
from dataclasses import dataclass
from typing import Literal, TypedDict

from typing_extensions import Self

from .base_objects import WorldstateObject, Record


class _OrbVallisRecord(Record, TypedDict):
    expiry: str
    activation: str
    timeLeft: str
    isWarm: bool


@dataclass(frozen=True, order=True)
class OrbVallis(WorldstateObject):
    expiry: datetime.datetime
    activation: datetime.datetime
    time_left: str
    is_warm: bool

    @classmethod
    def _from_response(cls: 'OrbVallis', response: _OrbVallisRecord) -> Self:
        return cls(
            activation=datetime.datetime.fromisoformat(response["activation"]),
            expiry=datetime.datetime.fromisoformat(response["expiry"]),
            time_left=response["timeLeft"],
            is_warm=response["isWarm"],
        )
