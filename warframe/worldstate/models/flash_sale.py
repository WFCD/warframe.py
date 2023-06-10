from datetime import datetime
from typing import Optional

from msgspec import field

from ..common import MultiQueryModel

__all__ = ["FlashSale"]


class FlashSale(MultiQueryModel):
    __endpoint__ = "/flashSales"

    # required
    item: str
    "The Item that is being sold"

    eta: str
    "Short-formatted string estimating the time until the Flash Sale ends"

    discount: int
    "The discount of the item."

    premium_override: int
    "The premium override of this item"

    # optional
    is_featured: Optional[bool] = None  # docs are wrong
    "Whether the item is featured"

    is_popular: Optional[bool] = None  # docs are wrong
    "Whether the item is popular"

    expired: Optional[bool] = None
    "Whether the item is expired or not"

    is_in_market: Optional[bool] = field(name="isShownInMarket", default=None)
    "Whether the item is available/shown in the market. Most likely to be `True`"

    expiry: Optional[datetime] = None
    "The time the Flash Sale ends"
