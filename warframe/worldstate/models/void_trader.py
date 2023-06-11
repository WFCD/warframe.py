from datetime import datetime
from typing import List, Optional

from msgspec import field

from ..common import SingleQueryModel, WorldstateObject, TimedEvent

__all__ = ["VoidTrader"]


class InventoryItem(WorldstateObject):
    item: str
    "The item that is being sold"

    ducats: int
    "The cost of ducats"

    credits: int
    "The cost of credits"


class VoidTrader(SingleQueryModel, TimedEvent):
    __endpoint__ = "/voidTrader"

    # required
    location: str
    "The Relay on which the Void Trader is on"

    inventory: List[InventoryItem]
    "The Void Trader's inventory"
