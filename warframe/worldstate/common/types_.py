from datetime import datetime
from typing import ClassVar, Literal, Protocol, Type, TypeVar

from .core import WorldstateObject

__all__ = ["ItemRewardType", "FissureTier", "FissureTierNumber", "_TimedAndSingleQuery"]

ItemRewardType = Literal[
    "vauban",
    "vandal",
    "wraith",
    "skin",
    "helmet",
    "nitain",
    "mutalist",
    "weapon",
    "fieldron",
    "detonite",
    "mutagen",
    "aura",
    "neuralSensors",
    "orokinCell",
    "alloyPlate",
    "circuits",
    "controlModule",
    "ferrite",
    "gallium",
    "morphics",
    "nanoSpores",
    "oxium",
    "rubedo",
    "salvage",
    "plastids",
    "polymerBundle",
    "argonCrystal",
    "cryotic",
    "tellurium",
    "neurodes",
    "nightmare",
    "endo",
    "reactor",
    "catalyst",
    "forma",
    "synthula",
    "exilus",
    "riven",
    "kavatGene",
    "kubrowEgg",
    "traces",
    "other",
    "credits",
]

FissureTier = Literal["Lith", "Meso", "Neo", "Axi", "Requiem"]

FissureTierNumber = Literal[1, 2, 3, 4, 5]

T = TypeVar("T", bound=WorldstateObject)


class _TimedAndSingleQuery(Protocol):
    __endpoint__: ClassVar[str]

    activation: datetime
    "The time the event began"

    expiry: datetime
    "The time the event ends"

    @property
    def start_string(self) -> str:
        "Short-time-formatted duration string representing the start of the event"
        ...

    @property
    def eta(self) -> str:
        "Short-time-formatted duration string representing the end of the event / cycle"
        ...

    @property
    def expired(self) -> bool:
        ...

    @property
    def active(self) -> bool:
        ...

    @classmethod
    def _from_json(cls: Type[T], response: str) -> T:
        ...
