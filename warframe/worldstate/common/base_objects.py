from datetime import datetime
from typing import Any, List, Type, TypeVar, ClassVar

import msgspec


__all__ = ["MultiQueryModel", "SingleQueryModel", "WorldstateObject"]


def _decode_hook(type: Type, obj: Any) -> Any:
    if isinstance(type, datetime) and isinstance(obj, str):
        return datetime.fromisoformat(obj.strip("Z"))

    return obj


class WorldstateObject(msgspec.Struct, rename="camel"):
    """
    Base class for every model-related object.
    """

    __endpoint__: ClassVar[str]


T = TypeVar("T", bound=WorldstateObject)


class MultiQueryModel(WorldstateObject):
    """
    Base class for giving models an indicator whether they can only come from a JSON array.
    """

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
