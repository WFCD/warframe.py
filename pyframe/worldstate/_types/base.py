from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import TypedDict

from typing_extensions import Self


class Record(TypedDict):
    pass


class WorldstateObject(ABC):
    @classmethod
    @abstractmethod
    def _from_response(cls, response: Record) -> Self:
        pass


@dataclass(frozen=True, order=True)
class Node:
    node: str
    node_key: str


class Faction(Enum):
    Grineer = 1
    Corpus = 2
    Infested = 3
    Orokin = 4
    Sentient = 5
    Narmer = 6


class MissionType(Enum):
    Arena = 1
    Assassination = 2
    Assault = 3
    Capture = 4
    Defection = 5
    Defense = 6
    MirrorDefense = 7
    Disruption = 8
    Excavation = 9
    Exterminate = 10
    FreeRoam = 11
    Heist = 12
    IsolationVault = 13
    Hijack = 14
    InfestedSalvage = 15
    Interception = 16
    Junction = 17
    MobileDefense = 18
    Orphix = 19
    Pursuit = 20
    Rescue = 21
    Rush = 22
    Sabotage = 23
    HiveSabotage = 24
    OrokinSabotage = 25
    ReactorSabotage = 26
    SealabSabotage = 27
    SanctuaryOnslaught = 28
    Skirmish = 29
    Spy = 30
    Survival = 31
    VoidArmageddon = 32
    VoidCascade = 33
    VoidFlood = 34
    Volatile = 35


class CountedItemRecord(Record):
    count: int
    type: str


class RewardRecord(Record):
    ...
