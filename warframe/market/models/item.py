from typing import List, Optional

import msgspec

from warframe.market.common import MarketObject, MultiQueryModel, SingleQueryModel


class ItemBase(MarketObject):
    thumb: str
    "The asset endpoint for the image of the Item"

    item_name: str
    "The item name of the item"

    @property
    def url_name(self) -> str:
        return "_".join(self.item_name.split(" ")).lower()


class MinimalItem(ItemBase, MultiQueryModel):
    __endpoint__ = "/items"
    __payload_name__ = "items"


class Item(MultiQueryModel):  # idk what to do here tbh
    __endpoint__ = "/items/<QUERY>"
    __payload_name__ = "item/items_in_set"

    icon: str
    icon_format: str

    sub_icon: Optional[str]
    mod_max_rank: Optional[int] = None
