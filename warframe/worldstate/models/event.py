from datetime import datetime
from typing import List, Optional

from msgspec import field

from .reward import Reward

from ..common import MultiQueryModel
from ..enums import MissionType, Faction, Syndicate

__all__ = ["Event"]


class Event(MultiQueryModel):
    activation: Optional[datetime] = None
    "The time the Event started"

    expiry: Optional[datetime] = None
    "The time the Event"

    start_string: Optional[str] = None
    "Short-time-formatted duration string of the start of the Fissure"

    active: Optional[bool] = None
    "Whether the event is currently active"

    maximum_score: Optional[int] = None
    "Maximum score to complete the event"

    current_score: Optional[int] = None
    "The current score for the event"

    small_interval: Optional[int] = None
    "Interval for the first goal"

    large_interval: Optional[int] = None
    "Interval for the second intermediate score"

    faction: Optional[Faction] = None
    "The faction you're up against"

    description: Optional[str] = None
    'The description or "subtitle" for the event'

    tooltip: Optional[str] = None
    "Tooltip for the event"

    node: Optional[str] = None
    "Node that the event is taking place on"

    concurrent_nodes: Optional[List[str]] = None
    "Nodes that the event is happening concurrently on"

    victim_node: Optional[str] = None
    "Node that is being attacked & defended in the event"

    score_loc_tag: Optional[str] = None
    "Localized tag for the event score"

    rewards: Optional[List[Reward]] = None
    "The rewards to earn"

    health: Optional[int] = None
    "Amount of health remaining for the target"

    affiliated_with: Optional[Syndicate] = None
    "The associated Syndicate"
