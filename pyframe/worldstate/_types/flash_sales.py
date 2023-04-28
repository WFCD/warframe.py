from dataclasses import dataclass
from typing import TypedDict

from typing_extensions import Self

from .base_objects import Record, WorldstateObject


class _FlashSaleRecord(Record, TypedDict):
    item: str
    expired: bool
    eta: str
    discount: int
    premium_override: int
    is_popular: bool
    is_featured: bool


@dataclass
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
        return [cls(
            item=response_item['item'],
            expired=response_item['expired'],
            eta=response_item['eta'],
            discount=response_item['discount'],
            premium_override=response_item['premiumOverride'],
            is_popular=response_item['isPopular'],
            is_featured=response_item['isFeatured']
        )
            for response_item
            in response
        ]
