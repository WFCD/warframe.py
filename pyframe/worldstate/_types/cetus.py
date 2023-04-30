import datetime
from dataclasses import dataclass
from typing import Literal, Optional

from typing_extensions import Self

from .base import WorldstateObject, Record


class _CetusRecord(Record):
    # required
    expiry: str
    isDay: bool
    timeLeft: str

    # optional
    activation: Optional[str]
    startString: Optional[str]
    active: Optional[bool]
    state: Optional[Literal["day", "night"]]
    shortString: Optional[str]


@dataclass(frozen=True, order=True)
class Cetus(WorldstateObject):
    # required
    expiry: datetime.datetime
    is_day: bool
    time_left: str

    # optional
    activation: Optional[datetime.datetime]
    start_string: Optional[str]
    active: Optional[bool]
    state: Optional[Literal["day", "night"]]
    short_string: Optional[str]

    @classmethod
    def _from_response(cls: "Cetus", response: _CetusRecord) -> Self:
        return cls(
            activation=datetime.datetime.fromisoformat(response.get("activation"))
            if "activation" in response
            else None,
            expiry=datetime.datetime.fromisoformat(response.get("expiry")),
            start_string=response.get("startString"),
            active=response.get("active"),
            is_day=response.get("isDay"),
            state=response.get("state"),
            time_left=response.get("timeLeft"),
            short_string=response.get("shortString"),
        )
