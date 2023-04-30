from dataclasses import dataclass
from typing import Optional

from typing_extensions import Self

from .base import Record, WorldstateObject


class _FlashSaleRecord(Record):
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


@dataclass(frozen=True, order=True)
class FlashSale(WorldstateObject):
    # required
    item: str
    eta: str
    discount: int
    premium_override: int
    is_popular: bool
    is_featured: bool

    # optional
    expired: Optional[bool]
    in_market: Optional[bool]
    eta: Optional[str]

    @classmethod
    def _from_response(cls, response: list[_FlashSaleRecord]) -> list[Self]:
        return [
            cls(
                item=response_item.get("item"),
                expired=response_item.get("expired"),
                eta=response_item.get("eta"),
                discount=response_item.get("discount"),
                premium_override=response_item.get("premiumOverride"),
                is_popular=response_item.get("isPopular"),
                is_featured=response_item.get("isFeatured"),
                expired=response_item.get("expired"),
                in_market=response_item.get("isShownInMarket"),
                eta=response_item.get("eta"),
            )
            for response_item in response
        ]
