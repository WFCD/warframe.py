import datetime
from dataclasses import dataclass

from typing_extensions import Self

from .base import WorldstateObject, Record


class _DailyDealRecord(Record):
    sold: int
    item: str
    total: int
    eta: str
    originalPrice: int
    salePrice: int
    discount: int
    expiry: str


@dataclass(frozen=True, order=True)
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
        return [
            cls(
                sold=response_item.get("sold"),
                item=response_item.get("item"),
                total_available=response_item.get("total"),
                eta=response_item.get("eta"),
                original_price=response_item.get("originalPrice"),
                sales_price=response_item.get("salePrice"),
                discount=response_item.get("discount"),
                expiry=datetime.datetime.fromisoformat(response_item["expiry"]),
            )
            for response_item in response
        ]
