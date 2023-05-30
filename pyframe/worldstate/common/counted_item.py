from dataclasses import dataclass

from .worldstate_object import WorldstateObject


@dataclass
class CountedItem(WorldstateObject):
    count: int
    type: str
