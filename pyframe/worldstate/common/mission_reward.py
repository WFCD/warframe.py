from typing import List

from .base_objects import WorldstateObject
from .counted_item import CountedItem

__all__ = ["MissionReward"]


class MissionReward(WorldstateObject):
    # required
    counted_items: List[CountedItem]
    "Items that have a quantity attached"
    thumbnail: str
    "Thumbnail URL"
    color: int
    "RGB value as an int assigned to this reward"
    credits: int
    "Amount of credits awarded"
    as_string: str
    "String representation of the reward"
    items: List[str]
    "Items' names possible to be won"
    item_string: str
    "formatted string describing all included items"
