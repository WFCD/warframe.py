from dataclasses import dataclass
from typing import List

from .worldstate_object import WorldstateObject
from .counted_item import CountedItem


class MissionReward(WorldstateObject):
    # required
    countedItems: List[CountedItem]
    "Items that have a quantity attached"
    thumbnail: str
    "Thumbnail URL"
    color: int
    "RGB value as an int assigned to this reward"
    credits: int
    "Amount of credits awarded"
    asString: str
    "String representation of the reward"
    items: List[str]
    "Items' names possible to be won"
    itemString: str
    "formatted string describing all included items"
