from enum import Enum

BASE_URL = "https://api.warframestat.us/pc"

__all__ = ["Language"]


class Endpoint(Enum):
    # Open Worlds
    CETUS = "/cetusCycle"
    CAMBION_DRIFT = "/cambionCycle"
    ORB_VALLIS = "/vallisCycle"

    # Darvo
    DAILY_DEAL = "/dailyDeals"
    FLASH_SALES = "/flashSales"

    # Alert related
    ALERTS = "/alerts"
    ARBITRATION = "/arbitration"
    INVASIONS = "/invasions"
    VOID_TRADER = "/voidTrader"
    EVENTS = "/events"
    NEWS = "/news"

    # Daily stuff
    ARCHON_HUNT = "/archonHunt"
    STEEL_PATH = "/steelPath"
    SORTIE = "/sortie"

    # Misc
    CONCLAVE = "/conclaveChallenges"
    CONSTRUCTION_PROGRESS = "/constructionProgress"
    EARTH_CYCLE = "/earthCycle"
    FISSURES = "/fissures"
    GLOBAL_UPGRADES = "/globalUpgrades"  # don't really know what this is for
    KUVA_MISSIONS = "/kuva"
    NIGHTWAVE = "/nightwave"
    PERSISTENT_ENEMIES = "/persistentEnemies"
    RIVENS = "/rivens"
    SENTIENT_OUTPOST = "/sentientOutposts"
    SANCTUARY = "/simaris"
    SYNDICATE_MISSIONS = "/syndicateMissions"


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
