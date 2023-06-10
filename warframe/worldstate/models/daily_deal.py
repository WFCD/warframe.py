from datetime import datetime
from typing import Optional

from ..common import MultiQueryModel

__all__ = ["DailyDeal"]


class DailyDeal(MultiQueryModel):
    __endpoint__ = "/dailyDeals"

    # required
    sold: int
    "The amount of items sold"

    item: str
    "The item that is being sold"

    total: int
    "Sorry, I really don't know what this is for"

    eta: str
    "Short-formatted string estimating the time until the Daily Deal ends"

    original_price: int
    "The original price of the item"

    sale_price: int
    "The discounted price of the item"

    discount: int
    "The discount as %"

    expiry: datetime
    "The time the Daily Deal ends ends"

    # optional
    activation: Optional[datetime] = None
