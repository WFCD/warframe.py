from enum import Enum

base_url = "https://api.warframestat.us/pc"

__all__ = [
    "Language"
]

class Endpoint(Enum):
    # Open Worlds
    CETUS = f"{base_url}/cetusCycle"
    CAMBION_DRIFT = f"{base_url}/cambionCycle"
    ORB_VALLIS = f"{base_url}/vallisCycle"

    # Darvo
    DAILY_DEAL = f"{base_url}/dailyDeals"
    FLASH_SALES = f"{base_url}/flashSales"

    # Alert related
    ALERTS = f"{base_url}/alerts"
    ARBITRATION = f"{base_url}/arbitration"
    INVASIONS = f"{base_url}/invasions"
    VOID_TRADER = f"{base_url}/voidTrader"
    EVENTS = f"{base_url}/events"
    NEWS = f"{base_url}/news"

    # Daily stuff
    ARCHON_HUNT = f"{base_url}/archonHunt"
    STEEL_PATH = f"{base_url}/steelPath"
    SORTIE = f"{base_url}/sortie"

    # Misc
    CONCLAVE = f"{base_url}/conclaveChallenges"
    CONSTRUCTION_PROGRESS = f"{base_url}/constructionProgress"
    EARTH_CYCLE = f"{base_url}/earthCycle"
    FISSURES = f"{base_url}/fissures"
    GLOBAL_UPGRADES = f"{base_url}/globalUpgrades"  # don't really know what this is for
    KUVA_MISSIONS = f"{base_url}/kuva"
    NIGHTWAVE = f"{base_url}/nightwave"
    PERSISTENT_ENEMIES = f"{base_url}/persistentEnemies"
    RIVENS = f"{base_url}/rivens"
    SENTIENT_OUTPOST = f"{base_url}/sentientOutposts"
    SANCTUARY = f"{base_url}/simaris"
    SYNDICATE_MISSIONS = f"{base_url}/syndicateMissions"


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


def build_enpoint(endpoint: Endpoint, language: Language = Language.EN):
    return f"{endpoint.value}/?language={language.value}"
