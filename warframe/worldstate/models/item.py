from datetime import datetime
from typing import List, Optional

from msgspec import field

from ..common import MultiQueryModel, SingleQueryModel, TimedEvent
from ..enums import Faction, MissionType, Syndicate
from .reward import Reward


class Patchlog(MultiQueryModel):
    name: str
    "The name of the Patchlog"

    date: datetime
    "The release date of the Patch"

    url: str
    "The URL to the Official Patchlogs"

    additions: str
    "Any additions, most likely to be empty"

    changes: str
    "The changes this Item has received in the Patch"

    fixes: str
    "Any fixes related to this Item"


class Item(SingleQueryModel):
    name: str
    "The name localized of the Item"

    unique_name: str
    "The i18n of the Item"
