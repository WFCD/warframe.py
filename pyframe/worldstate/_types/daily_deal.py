import datetime
from dataclasses import dataclass
from typing import TypedDict

from typing_extensions import Self

from .base_objects import WorldstateObject, Record


class _DailyDealRecord(Record, TypedDict):
    sold: int
    item: str
    total: int
    eta: str
    originalPrice: int
    salePrice: int
    discount: int
    expiry: str


@dataclass
class DailyDeal(WorldstateObject):
    sold: int
    item: str
    total_available: int
    eta: str
    original_price: int
    sales_price: int
    discount: int
    expiry: datetime.datetime

    @classmethod
    def _from_response(cls, response: list[_DailyDealRecord]) -> list[Self]:
        return [cls(
            sold=response_item['sold'],
            item=response_item['item'],
            total_available=response_item['total'],
            eta=response_item['eta'],
            original_price=response_item['originalPrice'],
            sales_price=response_item['salePrice'],
            discount=response_item['discount'],
            expiry=datetime.datetime.fromisoformat(response_item['expiry'])
        )
            for response_item
            in response
        ]
