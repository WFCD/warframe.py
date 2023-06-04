from ..common.base_objects import SingleQueryModel

__all__ = ["CountedItem"]


class CountedItem(SingleQueryModel):
    count: int
    type: str
