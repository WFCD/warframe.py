from typing import List, Optional

from ..common import SingleQueryModel
from ..enums import Faction, MissionType
from .reward import Reward

__all__ = ["Mission"]


class Mission(SingleQueryModel):
    # required
    reward: Reward
    "The mission's reward"
    node: str
    "The localized node string"
    faction: Faction
    "The faction that houses the node/mission"
    max_enemy_level: int
    min_enemy_level: int
    max_wave_num: int
    type: MissionType
    "The MissionType of the given mission (Capture, Spy, etc.)"
    nightmare: bool
    "Whether the mission is a nightmare mission"
    archwing_required: bool
    "Whether an archwing is required in order to play the mission"
    description: str
    "The mission's description"

    # optional
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
