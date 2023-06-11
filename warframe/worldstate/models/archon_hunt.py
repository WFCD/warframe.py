from typing import List

from ..common import SingleQueryModel, TimedEvent
from ..enums import Faction, MissionType

__all__ = ["ArchonHunt"]


class ArchonHuntMission(SingleQueryModel):  # archon hunt's mission is pretty different
    # required
    node: str
    "The localized node string"

    node_key: str
    "The node string"

    type: str
    "The localized MissionType of the given mission (Capture, Spy, etc.)"

    type_key: MissionType
    "The MissionType of the given mission (Capture, Spy, etc.)"

    archwing_required: bool
    "Whether an archwing is required in order to play the mission"

    advanced_spawners: List[str]
    "Array of strings denoting extra spawners for a mission"

    required_items: List[str]
    "Items required to enter the mission"

    level_auras: List[str]
    "Affectors for this mission"

    is_sharkwing: bool
    "Whether the mission takes place in a submerssible mission"


class ArchonHunt(SingleQueryModel, TimedEvent):
    __endpoint__ = "/archonHunt"

    # required
    missions: List[ArchonHuntMission]
    "The list of missions that have to be played in order to queue up for the rewards"

    boss: str
    "The archon you are going to fight against"

    faction: Faction
    "The faction you're up against: Narmer"
