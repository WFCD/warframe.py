import json
from datetime import datetime, timezone
from typing import Any, ClassVar, List, Optional, Type, TypeVar

import msgspec

__all__ = ["MarketObject", "SingleQueryModel", "MultiQueryModel"]


class MarketObject(msgspec.Struct):
    """
    Base class for every model-related object used by the market package.
    """

    pass


T = TypeVar("T", bound=MarketObject)


class Queryable(MarketObject):
    __endpoint__: ClassVar[str]
    __payload_name__: ClassVar[str]

    @classmethod
    def _from_json(cls: Type[T], response: str):
        raise NotImplementedError(
            "This function has to be overridden in a derived class."
        )


class SingleQueryModel(Queryable):
    @classmethod
    def _from_json(cls: Type[T], response: str) -> T:
        data = json.loads(response)["payload"]

        return msgspec.from_builtins(data, type=cls)


class MultiQueryModel(Queryable):
    @classmethod
    def _from_json(cls: Type[T], response: str) -> List[T]:
        data = json.loads(response)["payload"]

        return msgspec.from_builtins(data, type=List[cls])


class Drop(MarketObject):
    name: str
    link: str


class LanguageItem(MarketObject):
    item_name: str
    description: str
    wiki_link: str
    drops: List[Drop] = msgspec.field(name="drop")
