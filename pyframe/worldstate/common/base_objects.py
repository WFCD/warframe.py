from datetime import datetime
from typing import Any, List, Type, TypeVar, ClassVar

import msgspec

T = TypeVar("T")

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


class MultiQueryModel(WorldstateObject):
    """
    Base class for giving models an indicator whether they can only come from a JSON array.
    """

    @classmethod
    def _from_json(cls: Type[T], response: str) -> List[T]:
        return msgspec.json.decode(response, type=List[cls], dec_hook=_decode_hook)


class SingleQueryModel(WorldstateObject):
    """
    Base class for giving models an indicator whether they can only come from a single JSON object.
    """

    @classmethod
    def _from_json(cls: Type[T], response: str) -> T:
        return msgspec.json.decode(response, type=cls, dec_hook=_decode_hook)
