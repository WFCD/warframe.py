from datetime import datetime
from typing import Optional

from ..common import MultiQueryModel

__all__ = ["DailyDeal"]


class DailyDeal(MultiQueryModel):
    __endpoint__ = "/dailyDeals"

    # required
    sold: int
    item: str
    total: int
    eta: str
    original_price: int
    sale_price: int
    discount: int
    expiry: datetime

    # optional
    activation: Optional[datetime] = None
