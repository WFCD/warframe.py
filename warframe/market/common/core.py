from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any, ClassVar, List, Optional, Self, Type, TypeVar, Union

import msgspec

__all__ = ["MarketObject"]


class MarketObject(msgspec.Struct):
    """
    Base class for every model-related object used by the market package.
    """

    pass


class Queryable(MarketObject):
    __endpoint__: ClassVar[str]
    __payload_name__: ClassVar[str]
    __payload_type__: ClassVar[Type]

    @classmethod
    def _from_json(cls, response: dict) -> Union[Self, List[Self]]:
        if cls.__payload_type__ is object:
            if cls.__payload_name__:
                return msgspec.from_builtins(response[cls.__payload_name__], type=cls)
            return msgspec.from_builtins(response, type=cls)

        elif cls.__payload_type__ is List:
            if cls.__payload_name__:
                return msgspec.from_builtins(response[cls.__payload_name__], type=List[cls])
            return msgspec.from_builtins(response, type=List[cls])

        else:
            raise Exception(f"{cls.__name__}'s payload type is invalid!")


class Drop(MarketObject):
    name: str
    link: str


class LanguageItem(MarketObject):
    item_name: str
    description: str
    wiki_link: str
    drops: List[Drop] = msgspec.field(name="drop")
