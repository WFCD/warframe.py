import datetime
from dataclasses import dataclass
from typing import Literal, Optional

from typing_extensions import Self

from .base import WorldstateObject, Record


class _CetusRecord(Record):
    activation: Optional[str]
    expiry: str
    startString: Optional[str]
    active: Optional[bool]
    isDay: bool
    state: Optional[Literal["day", "night"]]
    timeLeft: str
    shortString: Optional[str]


@dataclass(frozen=True, order=True)
class Cetus(WorldstateObject):
    activation: Optional[datetime.datetime]
    expiry: datetime.datetime
    start_string: Optional[str]
    active: Optional[bool]
    is_day: bool
    state: Optional[Literal["day", "night"]]
    time_left: str
    short_string: Optional[str]

    @classmethod
    def _from_response(cls: "Cetus", response: _CetusRecord) -> Self:
        return cls(
            activation=datetime.datetime.fromisoformat(response["activation"])
            if "activation" in response
            else None,
            expiry=datetime.datetime.fromisoformat(response["expiry"])
            if "expiry" in response
            else None,
            start_string=response.get("startString"),
            active=response.get("active"),
            is_day=response.get("isDay"),
            state=response.get("state"),
            time_left=response.get("timeLeft"),
            short_string=response.get("shortString"),
        )
