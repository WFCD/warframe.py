from datetime import datetime
from typing import List, Optional

from msgspec import field

from ..common import ItemRewardType, MultiQueryModel, TimedEvent, WorldstateObject
from ..enums import Faction
from .reward import Reward

__all__ = ["Invasion"]


class InvasionMember(WorldstateObject):
    # optional
    reward: Reward
    "The reward of the mission."

    faction: str
    "The localized faction that houses the node/mission"
    faction_key: Faction
    "The faction that houses the node/mission"


class Defender(InvasionMember):
    pass


class Attacker(InvasionMember):
    pass


class Invasion(MultiQueryModel):
    __endpoint__ = "/invasions"

    # required
    activation: datetime
    "The time the Invasion began"

    completed: bool
    "Whether the Invasion is over"

    completion_percentage: float = field(name="completion")
    "Percantage of the Invasion's completion"

    count: int
    "How many fights have happened"

    description: str = field(name="desc")
    "The Invasion's description"

    eta: str
    "Short-formatted string estimating the time until the Invasion is closed"

    node: str
    "The localized node string"

    node_key: str
    "The node string"

    required_runs: int
    "The amount of runs required to qualify for the reward. (most likely 3)"

    vs_infested: bool = field(name="vsInfestation")
    "Whether the fight is against infested enemies"

    attacker: Attacker
    "The invading faction information"

    defender: Defender
    "The defending faction information"

    start_string: str
    "Short-time-formatted duration string of the start of the Invasion"

    reward_types: List[ItemRewardType]
    "A list of reward types"
