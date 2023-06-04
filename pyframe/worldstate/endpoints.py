from enum import Enum

from .enums import Language

BASE_URL = "https://api.warframestat.us/pc"

__all__ = ["Language"]

# TODO: Slowly remove this enum, remove the corresponding endpoint here as soon as the model is implemented
# or: leave a comment


class Endpoint(Enum):
    # Alert related
    Alert = "/alerts"  # still needs testing
    Invasion = "/invasions"  # return type: list

    VoidTrader = "/voidTrader"
    """
    Example response:
    {"id":"5d1e07a0a38e4a4fdd7cefca","activation":"2023-06-02T13:00:00.000Z","startString":"-1d 21h 4m 45s","expiry":"2023-06-04T13:00:00.000Z","active":true,"character":"Baro Ki'Teer","location":"Kronia Relay (Saturn)","inventory":[{"item":"Thrax Sigil","ducats":50,"credits":55000},{"item":"Primed Fever Strike","ducats":350,"credits":200000},{"item":"High Voltage","ducats":300,"credits":150000},{"item":"Prisma Tetra","ducats":400,"credits":50000},{"item":"Stalker Beacon","ducats":200,"credits":125000},{"item":"Baro Ki'teer Glyph","ducats":80,"credits":50000},{"item":"Weapon Glaive On Kill Buff Secondary","ducats":300,"credits":115000},{"item":"Ki'teer Kubrow Armor","ducats":500,"credits":250000},{"item":"Xiphos Prisma Skin","ducats":220,"credits":400000},{"item":"Ki'teer Razza Synadana","ducats":400,"credits":350000},{"item":"Quanta Aufeis Skin","ducats":300,"credits":300000},{"item":"Ki'teer Atmos Diadem","ducats":525,"credits":375000},{"item":"Prisma Grinlok","ducats":500,"credits":220000},{"item":"Pack Leader Emblem","ducats":50,"credits":50000},{"item":"Sima Luxxum Ornament","ducats":100,"credits":100000},{"item":"Paracesis Elixis Skin","ducats":350,"credits":350000},{"item":"Liset Prop Grineer Cutter","ducats":100,"credits":100000},{"item":"Prisma Dual Decurions","ducats":525,"credits":175000},{"item":"Deimos Veolicpod Prex","ducats":75,"credits":100000},{"item":"Mulciber Shoulder Plate","ducats":315,"credits":215000},{"item":"Mulciber Leg Plate","ducats":300,"credits":200000},{"item":"Mulciber Chest Plate","ducats":325,"credits":250000},{"item":"Ivara Leverian Povis Records Decoration","ducats":75,"credits":100000},{"item":"Fae Path Ephemera","ducats":15,"credits":1000},{"item":"Sands Of Inaros Blueprint","ducats":100,"credits":25000}],"psId":"5d1e07a0a38e4a4fdd7cefca25","endString":"2h 55m 14s","initialStart":"1970-01-01T00:00:00.000Z","schedule":[]}
    """

    Event = "/events"  # return type: list
    News = "/news"  # return type: list

    # Daily stuff
    ArchonHunt = "/archonHunt"
    SteelPath = "/steelPath"
    Sortie = "/sortie"

    # Misc
    Conclave = "/conclaveChallenges"
    ConstructionProgress = "/constructionProgress"
    EarthCycle = "/earthCycle"
    Fissure = "/fissures"  # return type: list
    GlobalUpgrade = (
        "/globalUpgrades"  # return type: list // modifiers (like double res weekend)
    )
    KuvaMission = "/kuva"  # return type: list
    Nightwave = "/nightwave"
    PersistentEnemy = "/persistentEnemies"  # return type: list
    Riven = "/rivens"  # return type: list
    SentientOutpost = "/sentientOutposts"
    Sanctuary = "/simaris"
    SyndicateMission = "/syndicateMissions"


def build_endpoint(endpoint: str, language: Language = Language.EN):
    return f"{BASE_URL}{endpoint}/?language={language.value}"
