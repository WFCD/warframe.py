from datetime import datetime
from typing import List, Optional

from msgspec import field

from ..common import SingleQueryModel
from ..enums import MissionType, Faction

__all__ = ["Sortie"]


class SortieMission(SingleQueryModel):
    node: str
    "The node the mission is on"
    type: MissionType = field(name="missionType")
    "The Type of the mission"
    modifier: str
    "The modifier applied to the mission"
    modifier_description: str
    "The description of the modifier"


class Sortie(SingleQueryModel):
    __endpoint__ = "/sortie"

    # required

    boss: str
    "The boss you're up against"
    activation: datetime
    "The time the Sortie started"
    expiry: datetime
    "The time the Sortie ends"
    missions: List[SortieMission] = field(name="variants")
    "The 3 missions you have to play in order to get the reward"
    faction: Faction
    "The Faction you're up against"
    expired: bool
    "Whether the Sortie is still active"
    eta: str
    "Short-formatted string estimating the time until the Sortie ends"

    # optional

    start_string: Optional[str] = None
    "Short-time-formatted duration string of the start of the Fissure"

    @property
    def active(self):
        return not self.expired
