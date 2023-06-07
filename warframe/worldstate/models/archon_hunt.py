from datetime import datetime
from typing import List, Optional

from ..common import SingleQueryModel
from ..enums import Faction, MissionType
from .reward import Reward

__all__ = ["ArchonHunt"]


class ArchonHuntMission(SingleQueryModel):  # archon hunt's mission is pretty different
    # required
    node: str
    "The localized node string"
    type: MissionType
    "The MissionType of the given mission (Capture, Spy, etc.)"
    nightmare: bool
    "Whether the mission is a nightmare mission"
    archwing_required: bool
    "Whether an archwing is required in order to play the mission"

    # optional
    reward: Optional[Reward] = None
    "The mission's reward"
    is_sharkwing: Optional[bool] = None
    "Whether the mission takes place in a submerssible mission"
    enemy_spec: Optional[str] = None
    "Enemy specification for the mission"
    level_override: Optional[str] = None
    "Override for the map on this mission"
    advanced_spawners: Optional[List[str]] = None
    "Array of strings denoting extra spawners for a mission"
    required_items: Optional[List[str]] = None
    "Items required to enter the mission"
    consume_required_items: Optional[bool] = None
    "Whether the required items are consumed"
    leaders_always_allowed: Optional[bool] = None
    "Whether leaders are always allowed"
    level_auras: Optional[List[str]] = None
    "Affectors for this mission"


class ArchonHunt(SingleQueryModel):
    __endpoint__ = "/archonHunt"

    # required
    activation: datetime
    "The time the Archon Hunt started"
    expiry: datetime
    "The time the Archon Hunt ends"
    missions: List[ArchonHuntMission]
    "The list of missions that have to be played in order to queue up for the rewards"
    boss: str
    "The archon you are going to fight against"
    faction: Faction
    "The faction you're up against: Narmer"
    expired: bool
    "Whether the Archon Hunt has ended"
    eta: str
    "Short-formatted string estimating the time until the Alert is closed."

    # optional
    start_string: Optional[str] = None
    "Short-time-formatted duration string representing the start of the Archon Hunt"
    active: Optional[bool] = None
    "Whether the alert is still active or not"
