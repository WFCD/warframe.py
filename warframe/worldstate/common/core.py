from datetime import datetime, timezone
from typing import Any, ClassVar, List, Type, TypeVar

import msgspec

__all__ = ["MultiQueryModel", "SingleQueryModel", "WorldstateObject", "TimedEvent"]


def _decode_hook(type: Type, obj: Any) -> Any:
    if isinstance(type, datetime) and isinstance(obj, str):
        return datetime.fromisoformat(obj.strip("Z"))

    return obj


def _get_short_format_time_string(dt: datetime) -> str:
    """
    Returns a short time formatted string based on the current time and the specified datetime.

    Parameters
    ----------
    dt : datetime
        The time the event started/ended.

    Returns
    -------
    str
        The short time formatted string representing the time difference between now and the specified datetime.
    """

    now = datetime.now(tz=timezone.utc)
    time_in_between = now - dt if now > dt else dt - now

    days = time_in_between.days
    hours, remainder = divmod(time_in_between.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    time_components = [(days, "d"), (hours, "h"), (minutes, "m"), (seconds, "s")]
    formatted_time = ""

    for t, suffix in time_components:
        if t != 0:
            formatted_time += f"{t}{suffix} "

    return formatted_time.strip()


class TimedEvent(msgspec.Struct, rename="camel"):
    activation: datetime
    "The time the event began"

    expiry: datetime
    "The time the event ends"

    @property
    def start_string(self) -> str:
        "Short-time-formatted duration string representing the start of the event"
        return f"{_get_short_format_time_string(self.activation)} ago"

    @property
    def eta(self) -> str:
        "Short-time-formatted duration string representing the end of the event / cycle"
        return _get_short_format_time_string(self.expiry)

    @property
    def expired(self) -> bool:
        return self.activation >= self.expiry

    @property
    def active(self) -> bool:
        return not self.expired


class WorldstateObject(msgspec.Struct, rename="camel"):
    """
    Base class for every model-related object.
    """

    pass


T = TypeVar("T", bound=WorldstateObject)


class MultiQueryModel(WorldstateObject):
    """
    Base class for giving models an indicator whether they can only come from a JSON array.
    """

    __endpoint__: ClassVar[str]

    @classmethod
    def _from_json(cls: Type[T], response: str) -> List[T]:
        """
        Decodes a JSON string to a list of objects of type T.

        Parameters
        ----------
        cls : Type[T]
            The type T.
        response : str
            The raw JSON as a string.

        Returns
        -------
        List[T]
            A list of objects of type T.
        """

        return msgspec.json.decode(response, type=List[cls], dec_hook=_decode_hook)


class SingleQueryModel(WorldstateObject):
    """
    Base class for giving models an indicator whether they can only come from a single JSON object.
    """

    __endpoint__: ClassVar[str]

    @classmethod
    def _from_json(cls: Type[T], response: str) -> T:
        """
        Decodes a JSON string to an object of type T.

        Parameters
        ----------
        cls : Type[T]
            The type T.
        response : str
            The raw JSON as a string.

        Returns
        -------
        T
            The object of type T.
        """

        return msgspec.json.decode(response, type=cls, dec_hook=_decode_hook)
