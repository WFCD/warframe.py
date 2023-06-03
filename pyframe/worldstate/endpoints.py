from enum import Enum
from typing import Type

from .common import WorldstateObject

BASE_URL = "https://api.warframestat.us/pc"

__all__ = ["Language"]


class Endpoint(Enum):
    # Open Worlds
    Cetus = "/cetusCycle"
    CambionDrift = "/cambionCycle"
    OrbVallis = "/vallisCycle"

    # Darvo
    DailyDeal = "/dailyDeals"
    FlashSale = "/flashSales"  # return type: list

    # Alert related
    Alert = "/alerts"  # return type: list
    Arbitration = "/arbitration"
    Invasion = "/invasions"  # return type: list
    VoidTrader = "/voidTrader"
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


class Language(Enum):
    DE = "de"
    ES = "es"
    FR = "fr"
    IT = "it"
    KO = "ko"
    PL = "pl"
    PT = "pt"
    RU = "ru"
    ZH = "zh"
    EN = "en"
    UK = "uk"

    German = DE
    Spanish = ES
    French = FR
    Italian = IT
    Korean = KO
    Polish = PL
    Portuguese = PT
    Russian = RU
    Chinese = ZH
    English = EN
    Ukrainian = UK


def build_endpoint(endpoint: Endpoint, language: Language = Language.EN):
    return f"{BASE_URL}{endpoint.value}/?language={language.value}"


def endpoint_from_type(cls: Type[WorldstateObject]) -> Endpoint:
    return Endpoint.__members__[cls.__name__]
