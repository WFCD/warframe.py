from ..common import SingleQueryModel

__all__ = ["CountedItem"]


class CountedItem(SingleQueryModel):
    count: int
    "How many of the item"

    type: str
    "The type of the item"
