from .base_objects import WorldstateObject

__all__ = ["CountedItem"]


class CountedItem(WorldstateObject):
    count: int
    type: str
