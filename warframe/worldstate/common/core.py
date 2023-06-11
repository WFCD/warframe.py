from datetime import datetime
from typing import Any, List, Optional, Type, TypeVar, ClassVar

import msgspec


__all__ = ["MultiQueryModel", "SingleQueryModel", "WorldstateObject"]


def _decode_hook(type: Type, obj: Any) -> Any:
    if isinstance(type, datetime) and isinstance(obj, str):
        return datetime.fromisoformat(obj.strip("Z"))

    return obj


def get_start_string(activation: datetime) -> str:
    """Returns an short time formatted string based on the activation.

    Args:
        activation (datetime): The time the Event XYZ started

    Returns:
        str: The short time formatted string of the time in between now and when the event started.
    """
    time_in_between = datetime.now() - activation

    days = time_in_between.days
    hours, remainder = divmod(time_in_between.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    time_components = [(days, "d"), (hours, "h"), (minutes, "m"), (seconds, "s")]
    formatted_time = ""

    for t, suffix in time_components:
        if t != 0:
            formatted_time += f"{t}{suffix} "

    return formatted_time.strip()


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
        """Decodes a JSON string to an list of object of T.

        Args:
            cls (Type[T]): The type T.
            response (str): The raw JSON as string.

        Returns:
            List[T]: A list of objects of T.
        """
        return msgspec.json.decode(response, type=List[cls], dec_hook=_decode_hook)


class SingleQueryModel(WorldstateObject):
    """
    Base class for giving models an indicator whether they can only come from a single JSON object.
    """

    __endpoint__: ClassVar[str]

    @classmethod
    def _from_json(cls: Type[T], response: str) -> T:
        """Decodes a JSON string to an object of T.

        Args:
            cls (Type[T]): The type T.
            response (str): The raw JSON as string.

        Returns:
            T: The object of T
        """
        return msgspec.json.decode(response, type=cls, dec_hook=_decode_hook)
