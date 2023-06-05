from datetime import datetime
from typing import List, Optional

from ..common import ItemRewardType, MultiQueryModel
from .mission import Mission

__all__ = ["Alert"]


class Alert(MultiQueryModel):
    __endpoint__ = "/alerts"

    # required
    mission: Mission
    "The mission that corresponds to this Alert"
    expired: bool
    "Whether the mission is expired or not"
    reward_types: List[ItemRewardType]
    "A list of reward types"

    # optional
    activation: Optional[datetime] = None
    "The time the mission began"
    expiry: Optional[datetime] = None
    "The time the mission ends"
    start_string: Optional[str] = None
    "Short-time-formatted duration string representing the start of the alert"
    active: Optional[bool] = None
    "Whether the alert is still active or not"
    eta: Optional[str] = None
    "Short-formatted string estimating the time until the Alert is closed"
