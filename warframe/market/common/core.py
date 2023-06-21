from datetime import datetime, timezone
from typing import Any, List, Optional, Type, TypeVar, ClassVar

import msgspec

__all__ = ["MarketObject", "PayloadItemCollection", "Payload"]


class MarketObject(msgspec.Struct):
    """
    Base class for every model-related object used by the market package.
    """

    pass


class PayloadItemCollection(MarketObject):
    pass


class Payload(MarketObject):
    payload: Type[PayloadItemCollection]
