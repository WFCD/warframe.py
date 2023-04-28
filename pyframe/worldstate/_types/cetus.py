import datetime
from dataclasses import dataclass
from typing import Literal, TypedDict

from typing_extensions import Self

from .base_objects import WorldstateObject, Record


class _CetusRecord(Record, TypedDict):
    activation: str
    expiry: str
    startString: str
    active: bool
    isDay: bool
    state: Literal["day", "night"]
    timeLeft: str
    shortString: str


@dataclass(frozen=True, order=True)
class Cetus(WorldstateObject):
    activation: datetime.datetime
    expiry: datetime.datetime
    start_string: str
    active: bool
    is_day: bool
    state: Literal["day", "night"]
    time_left: str
    short_string: str

    @classmethod
    def _from_response(cls: 'Cetus', response: _CetusRecord) -> Self:
        return cls(
            activation=datetime.datetime.fromisoformat(response["activation"]),
            expiry=datetime.datetime.fromisoformat(response["expiry"]),
            start_string=response["startString"],
            active=response["active"],
            is_day=response["isDay"],
            state=response["state"],
            time_left=response["timeLeft"],
            short_string=response["shortString"],
        )
