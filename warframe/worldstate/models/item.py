from datetime import datetime
from typing import Any, List, Optional

from msgspec import field

from ..common import MultiQueryModel, SingleQueryModel, TimedEvent
from ..enums import Category, Faction, ItemType, MissionType, ProductCategory, Syndicate
from .reward import Reward


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

    drops: List[Any]  # help tobi?
    "idk"

    masterable: bool
    "Whether the Item can be mastered"


class ShallowItem(MultiQueryModel):
    unique_name: str
    "The i18n of the Item"

    name: str
    "The name localized of the Item"

    description: str
    "The localized description of the Item"

    item_count: int
    "The amount of Items needed"

    image_name: str
    "The name of the image of the Item"

    tradable: bool
    "Whether the Item is tradable or not"

    type: ItemType
    "The type of this Item"


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

    estimated_vault_date: Optional[datetime] = None
    "The estimated vault date of this Item"

    introduction: Optional[Introduction] = None
    "The introduction of this item.\nNOTE: It's an own object."
