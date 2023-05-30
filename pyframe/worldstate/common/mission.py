from dataclasses import dataclass
from typing import List, Optional

from .worldstate_object import WorldstateObject
from ..enums import Faction, MissionType


@dataclass(frozen=True, order=True)
class Mission(WorldstateObject):
    # required
    reward: ...
    "The mission's reward"
    node: str
    "The localized node string"
    faction: Faction
    "The Faction of the mission"
    maxEnemyLevel: int
    minEnemyLevel: int
    maxWaveNum: int
    type: MissionType
    "The MissionType of the given mission (Capture, Spy, etc.)"
    nightmare: bool
    "Whether the mission is a nightmare mission"
    archwingRequired: bool
    "Whether an archwing is required in order to play the mission"
    description: str
    "The mission's description"

    # optional
    isSharkwing: Optional[bool]
    "Whether the mission takes place in a submerssible mission"
    enemySpec: Optional[str]
    "Enemy specification for the mission"
    levelOverride: Optional[str]
    "Override for the map on this mission"
    advancedSpawners: Optional[List[str]]
    "Array of strings denoting extra spawners for a mission"
    requiredItems: Optional[List[str]]
    "Items required to enter the mission"
    consumeRequiredItems: Optional[bool]
    "Whether the required items are consumed"
    leadersAlwaysAllowed: Optional[bool]
    "Whether leaders are always allowed"
    levelAuras: Optional[List[str]]
    "Affectors for this mission"
