import datetime
from dataclasses import dataclass
from typing import Optional

from typing_extensions import Self

from .base import WorldstateObject, Record


class _DailyDealRecord(Record):
    # required
    sold: int
    item: str
    total: int
    eta: str
    originalPrice: int
    salePrice: int
    discount: int
    expiry: str

    # optional
    activation: Optional[str]


@dataclass(frozen=True, order=True)
class DailyDeal(WorldstateObject):
    # required
    sold: int
    item: str
    total_available: int
    eta: str
    original_price: int
    sales_price: int
    discount: int
    expiry: datetime.datetime

    # optional
    activation: Optional[datetime.datetime]

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
                expiry=datetime.datetime.fromisoformat(response_item.get("expiry")),
                activation=datetime.datetime.fromisoformat(
                    response_item.get("activation")
                )
                if "activation" in response_item
                else None,
            )
            for response_item in response
        ]
