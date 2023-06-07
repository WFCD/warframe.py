from datetime import datetime
from typing import Optional

from msgspec import field
from ..common import MultiQueryModel, FissureTier, FissureTierNumber
from ..enums import MissionType, Faction

__all__ = ["Fissure"]


class Fissure(MultiQueryModel):
    __endpoint__ = "/fissures"

    # required
    activation: datetime
    "The time the Fissure started"
    expiry: datetime
    "The time the fissure ends"
    node: str
    "The localized node string"
    expired: bool
    "Whether the fissure is still present"
    eta: str
    "Short-formatted string estimating the time until the Fissure is closed"
    mission_type: MissionType
    "The game mode that the mission/node houses"
    tier: FissureTier
    "Tier of the mission (Lith, Meso, etc.)"
    tier_num: FissureTierNumber
    "The Numeric tier corresponding to the tier"
    faction: Faction = field(name="enemy")
    "The faction that houses the node/mission"
    is_steel_path: bool = field(name="isHard")
    "Whether the mission of the Fissure is on is on the Steel Path"
    is_railjack: bool = field(name="isStorm")
    "Whether the mssion of the Fissure is a Railjack mission"

    # optional
    start_string: Optional[str] = None
    "Short-time-formatted duration string of the start of the Fissure"
    active: Optional[bool] = None
    "Whether the fissure is currently active"
