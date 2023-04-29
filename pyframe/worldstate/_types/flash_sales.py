from dataclasses import dataclass

from typing_extensions import Self

from .base import Record, WorldstateObject


class _FlashSaleRecord(Record):
    item: str
    expired: bool
    eta: str
    discount: int
    premium_override: int
    is_popular: bool
    is_featured: bool


@dataclass(frozen=True, order=True)
class FlashSale(WorldstateObject):
    item: str
    expired: bool
    eta: str
    discount: int
    premium_override: int
    is_popular: bool
    is_featured: bool

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
            )
            for response_item in response
        ]
