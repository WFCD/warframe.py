from typing import List
from warframe.market.common import MarketObject, Payload, PayloadItemCollection
import msgspec


class MinimalItem(MarketObject):
    thumb: str
    "The asset endpoint for the image of the Item"

    item_name: str
    "The item name of the item"

    @property
    def url_name(self) -> str:
        return "_".join(self.item_name.split(" ")).lower()


class ItemPayload:  # idk what to do here tbh
    ...
