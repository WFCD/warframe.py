from .base_objects import WorldstateObject


class CountedItem(WorldstateObject):
    count: int
    type: str
