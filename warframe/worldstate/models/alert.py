from datetime import datetime
from typing import List, Optional

from ..common import ItemRewardType, MultiQueryModel
from .mission import Mission

__all__ = ["Alert"]


class Alert(MultiQueryModel):
    __endpoint__ = "/alerts"

    # required
    activation: datetime
    "The time the mission began"

    expiry: datetime
    "The time the mission ends"

    mission: Mission
    "The mission that corresponds to this Alert"

    reward_types: List[ItemRewardType]
    "A list of reward types"

    # optional
    start_string: Optional[str] = None
    "Short-time-formatted duration string representing the start of the alert"

    active: Optional[bool] = None
    "Whether the alert is still active or not"

    eta: Optional[str] = None
    "Short-formatted string estimating the time until the Alert is closed"

    expired: Optional[bool] = None
    "Whether the mission is expired or not"
