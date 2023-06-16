from msgspec import field

from ..common import FissureTier, FissureTierNumber, MultiQueryModel, TimedEvent
from ..enums import Faction, MissionType

__all__ = ["Fissure"]


class Fissure(MultiQueryModel, TimedEvent):
    __endpoint__ = "/fissures"

    # required
    node: str
    "The localized node string"

    node: str
    "The localized node string"

    node_key: str
    "The node string"

    mission_type: str
    "The localized game mode that the mission/node houses"

    mission_type_key: MissionType = field(name="missionKey")
    "The game mode that the mission/node houses"

    tier: FissureTier
    "Tier of the mission (Lith, Meso, etc.)"

    tier_num: FissureTierNumber
    "The Numeric tier corresponding to the tier"

    faction: str = field(name="enemy")
    "The localized faction that houses the node/mission"

    faction_key: Faction = field(name="enemyKey")
    "The faction that houses the node/mission"

    is_steel_path: bool = field(name="isHard")
    "Whether the mission of the Fissure is on is on the Steel Path"

    is_railjack: bool = field(name="isStorm")
    "Whether the mssion of the Fissure is a Railjack mission"
