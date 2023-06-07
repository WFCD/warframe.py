from datetime import datetime
from typing import List, Optional

from msgspec import field

from ..common import SingleQueryModel

__all__ = ["VoidTrader"]


class InventoryItem(SingleQueryModel):
    __endpoint__ = ""

    item: str
    "The item that is being sold"
    ducats: int
    "The cost of ducats"
    credits: int
    "The cost of credits"


class VoidTrader(SingleQueryModel):
    __endpoint__ = "/voidTrader"

    # required

    start_string: str
    "Short-time-formatted duration string of the arrival of the Void Trader"
    active: bool
    "Whether the Void Trader is currently active"
    location: str
    "The Relay on which the Void Trader is on"
    inventory: List[InventoryItem]
    "The Void Trader's inventory"
    end_string: str
    "Short-time-formatted duration string of the department of the Void Trader"

    # optional
    arrival: Optional[datetime] = field(name="activation", default=None)
    "The time the Void Trader arrived"
    department: Optional[datetime] = field(name="expiry", default=None)
    "The time the Void Trader departs"
