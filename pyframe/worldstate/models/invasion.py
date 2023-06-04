from datetime import datetime
from typing import List, Optional

from msgspec import field

from ..common import ItemRewardType, MultiQueryModel, SingleQueryModel
from ..enums import Faction
from .reward import Reward

__all__ = ["Invasion"]


class InvasionMember(SingleQueryModel):
    __endpoint__ = ""

    # optional
    reward: Optional[Reward] = None
    "The reward of the mission."
    faction: Optional[Faction] = None
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
    required_runs: int
    "The amount of runs required to qualify for the reward. (most likely 3)"
    vs_infested: bool = field(name="vsInfestation")
    "Whether the fight is against infested enemies"

    # optional
    expiry: Optional[datetime] = None
    "The time the Invasion ends"
    start_string: Optional[str] = None
    "Short-time-formatted duration string of the start of the Invasion"
    active: Optional[bool] = None
    "Whether the invasion is currently active"
    attacker: Optional[Attacker] = None
    "The invading faction information"
    defender: Optional[Defender] = None
    "The defending faction information"
    reward_types: Optional[List[ItemRewardType]] = None
    "A list of reward types"
