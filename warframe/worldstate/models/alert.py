from typing import List

from ..common import ItemRewardType, MultiQueryModel, TimedEvent
from .mission import Mission

__all__ = ["Alert"]


class Alert(MultiQueryModel, TimedEvent):
    __endpoint__ = "/alerts"

    # required
    mission: Mission
    "The mission that corresponds to this Alert"

    reward_types: List[ItemRewardType]
    "A list of reward types"
