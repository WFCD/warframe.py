from datetime import datetime
from typing import Optional

from msgspec import field

from ..common import SingleQueryModel
from ..enums import Faction, MissionType

__all__ = ["Arbitration"]


class Arbitration(SingleQueryModel):
    __endpoint__ = "/arbitration"

    # required
    activation: datetime
    "The time the mission began."
    expiry: datetime
    "The time the mission ends."
    node: str
    "The plain name for the node the Arbitration is on."
    faction: Faction = field(
        name="enemy"
    )  # it's not called faction at the endpoint, instead it's called enemy
    "The Faction of the corresponding mission."
    archwing_required: bool = field(name="archwing")
    "Whether an archwing is required in order to play the mission"
    is_sharkwing: bool = field(name="sharkwing")
    "Whether the mission takes place in a submerssible mission"

    # optional
    start_string: Optional[str] = None
    "Short-time-formatted duration string representing the start of the Arbitration."
    active: Optional[bool] = None
    "Whether the alert is still active or not."
    mission_type: Optional[MissionType] = None
    "The MissionType of the given mission (Capture, Spy, etc.)"
