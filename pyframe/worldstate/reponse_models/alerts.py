from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


from ..common import WorldstateObject, Mission, ItemRewardType


# TODO: IMPLEMENT REWARDS to be another type (https://docs.warframestat.us/#tag/Worldstate/operation/getAlertsByPlatform)

__all__ = ["AlertMission", "Alert"]


@dataclass(frozen=True, order=True)
class Alert(WorldstateObject):
    # required
    mission: Mission
    expired: bool
    rewardTypes: List[ItemRewardType]

    # optional
    activation: Optional[datetime]
    expiry: Optional[datetime]
    start_string: Optional[str]
    active: Optional[bool]
    eta: Optional[str]
