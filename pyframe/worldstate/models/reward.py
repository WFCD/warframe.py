from typing import List

from ..common import SingleQueryModel
from .counted_item import CountedItem

__all__ = ["Reward"]


class Reward(SingleQueryModel):
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
