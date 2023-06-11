from datetime import datetime
from typing import Optional

from msgspec import field

from ..common import MultiQueryModel, TimedEvent

__all__ = ["FlashSale"]


class FlashSale(MultiQueryModel, TimedEvent):
    __endpoint__ = "/flashSales"

    # required
    item: str
    "The Item that is being sold"

    discount: int
    "The discount of the item."

    premium_override: int
    "The premium override of this item"

    # optional
    is_featured: Optional[bool] = None  # docs are wrong
    "Whether the item is featured"

    is_popular: Optional[bool] = None  # docs are wrong
    "Whether the item is popular"

    is_in_market: Optional[bool] = field(name="isShownInMarket", default=None)
    "Whether the item is available/shown in the market. Most likely to be `True`"
