from datetime import datetime
from typing import Optional

from msgspec import field

from ..common import SupportsMany, WorldstateObject

__all__ = ["FlashSale"]


class FlashSale(WorldstateObject, SupportsMany):
    # required
    item: str
    eta: str
    discount: int
    premium_override: int

    # optional
    is_featured: Optional[bool] = None  # docs are wrong
    is_popular: Optional[bool] = None  # docs are wrong
    expired: Optional[bool] = None
    is_in_market: Optional[bool] = field(name="isShownInMarket", default=None)
    expiry: Optional[datetime] = None
