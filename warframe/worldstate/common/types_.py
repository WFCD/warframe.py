from typing import Literal

__all__ = ["ItemRewardType", "FissureTier", "FissureTierNumber"]

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
