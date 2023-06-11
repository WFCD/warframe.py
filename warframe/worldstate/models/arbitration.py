from typing import Optional

from msgspec import field

from ..common import SingleQueryModel, TimedEvent
from ..enums import Faction, MissionType

__all__ = ["Arbitration"]


class Arbitration(SingleQueryModel, TimedEvent):
    """
    UNSTABLE
    """

    __endpoint__ = "/arbitration"

    # required
    node: str
    "The localized plain name for the node the Arbitration is on."

    node_key: str
    "The plain name for the node the Arbitration is on."

    faction: Faction = field(
        name="enemy"
    )  # it's not called faction at the endpoint, instead it's called enemy
    "The Faction of the corresponding mission."

    archwing_required: bool = field(name="archwing")
    "Whether an archwing is required in order to play the mission"

    is_sharkwing: bool = field(name="sharkwing")
    "Whether the mission takes place in a submerssible mission"

    mission_type: str = field(name="type")
    "The localized MissionType of the given mission (Capture, Spy, etc.)"

    mission_type_key: MissionType = field(name="typeKey")
    "The MissionType of the given mission (Capture, Spy, etc.)"
