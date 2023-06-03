from datetime import datetime
from typing import Any, List, Type, TypeVar

import msgspec

T = TypeVar("T")


class SupportsMany:
    """
    Base class for giving models an indicator whether they can only come from a JSON array.
    """

    pass


class SupportsSingle:
    """
    Base class for giving models an indicator whether they can only come from a single JSON object.
    """

    pass


def _decode_hook(type: Type, obj: Any) -> Any:
    if isinstance(type, datetime) and isinstance(obj, str):
        return datetime.fromisoformat(obj.strip("Z"))

    return obj


class WorldstateObject(msgspec.Struct, rename="camel"):
    @classmethod
    def _from_json(cls: Type[T], response: str) -> T:
        return msgspec.json.decode(response, type=cls, dec_hook=_decode_hook)

    @classmethod
    def _many_from_json(cls: Type[T], response: str) -> List[T]:
        return msgspec.json.decode(response, type=List[cls], dec_hook=_decode_hook)
