from datetime import datetime
from typing import Any, List, Optional

import msgspec
from msgspec import field

from ..common import MultiQueryModel, SingleQueryModel, TimedEvent, WorldstateDT
from ..enums import (
    Category,
    Faction,
    ItemRarity,
    ItemType,
    MissionType,
    ProductCategory,
    Syndicate,
)


class Drop(MultiQueryModel):
    chance: float
    location: str
    rarity: ItemRarity
    type: str


class Introduction(SingleQueryModel):
    name: str
    "The name of the update"

    url: str
    "The url to this update"

    aliases: List[str]
    "The aliases of the update"

    parent: str
    "The parent update of this update"

    date: datetime
    "The actual date of the item's introduction"


class Patchlog(MultiQueryModel):
    name: str
    "The name of the Patchlog"

    date: datetime
    "The release date of the Patch"

    url: str
    "The URL to the Official Patchlogs"

    additions: str
    "Any additions, most likely to be empty"

    changes: str
    "The changes this Item has received in the Patch"

    fixes: str
    "Any fixes related to this Item"

    drops: List[Any] = []  # help tobi?
    "idk"

    masterable: Optional[bool] = None
    "Whether the Item can be mastered"


class ShallowItem(MultiQueryModel):
    unique_name: str
    "The i18n of the Item"

    name: str
    "The name localized of the Item"

    description: str
    "The localized description of the Item"

    image_name: str
    "The name of the image of the Item"

    tradable: bool
    "Whether the Item is tradable or not"

    count: int = msgspec.field(name="itemCount")
    "The amount of Items needed"

    drops: List[Drop] = []
    # type: ItemType
    # "The type of this Item"


class Item(SingleQueryModel):
    name: str
    "The name localized of the Item"

    unique_name: str
    "The i18n of the Item"

    type: ItemType
    "The type of this Item"

    tradable: bool
    "Whether the Item is tradable or not"

    category: Category
    "The category of this Item"

    patchlogs: List[Patchlog] = []
    "The patchlogs for this Item"

    components: List[ShallowItem] = []
    "The components needed for this Item"

    description: Optional[str] = None
    "The localized description of the Item"

    product_category: Optional[ProductCategory] = None
    "The product category of this Item"

    estimated_vault_date: Optional[WorldstateDT] = None
    "The estimated vault date of this Item"

    introduction: Optional[Introduction] = None
    "The introduction of this item.\nNOTE: It's an own object."
