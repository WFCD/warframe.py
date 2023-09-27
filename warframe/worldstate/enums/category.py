from enum import Enum

__all__ = ["Category"]


class Category(Enum):
    Warframes = "Warframes"
    Primary = "Primary"
    Secondary = "Secondary"
    Melee = "Melee"
    Sentinels = "Sentinels"
    Pets = "Pets"
    Archwing = "Archwings"
    ArchGuns = "Arch-Guns"
    ArchMelee = "Arch-Melee"
    Misc = "Misc"
