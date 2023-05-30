from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from ..common import WorldstateObject

__all__ = ["FlashSale"]


@dataclass(frozen=True, order=True)
class FlashSale(WorldstateObject):
    # required
    item: str
    eta: str
    discount: int
    premiumOverride: int
    isPopular: bool
    isFeatured: bool

    # optional
    expired: Optional[bool]
    isShownInMarket: Optional[bool]
    eta: Optional[str]
    expiry: Optional[datetime]
