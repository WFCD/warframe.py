from typing import List, Optional

from msgspec import field

from ..common import SingleQueryModel, TimedEvent
from ..enums import MissionType, Faction

__all__ = ["Sortie"]


class SortieMission(SingleQueryModel):
    node: str
    "The localized node the mission is on"

    type: str = field(name="missionType")
    "The localized Type of the mission"

    modifier: str
    "The modifier applied to the mission"

    modifier_description: str
    "The description of the modifier"


class Sortie(SingleQueryModel, TimedEvent):
    __endpoint__ = "/sortie"

    # required
    boss: str
    "The boss you're up against"

    missions: List[SortieMission] = field(name="variants")
    "The 3 missions you have to play in order to get the reward"

    faction: Faction
    "The Faction you're up against"
