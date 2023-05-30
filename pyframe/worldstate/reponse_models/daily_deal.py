from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from ..common import WorldstateObject

__all__ = ["DailyDeal"]


@dataclass(frozen=True, order=True)
class DailyDeal(WorldstateObject):
    # required
    sold: int
    item: str
    total: int
    eta: str
    originalPrice: int
    salePrice: int
    discount: int
    expiry: datetime

    # optional
    activation: Optional[datetime]
