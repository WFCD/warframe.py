from enum import Enum

class Endpoint(Enum):
    GENERAL = "https://api.warframestat.us/pc"

    # Open Worlds
    CETUS = "https://api.warframestat.us/pc/cetusCycle"
    CAMBION_DRIFT = "https://api.warframestat.us/pc/cambionCycle"
    ORB_VALLIS = "https://api.warframestat.us/pc/vallisCycle"

    # Darvo
    DAILY_DEAL = "https://api.warframestat.us/pc/dailyDeals"
    FLASH_SALES = "https://api.warframestat.us/pc/flashSales"

    # Alert related
    ALERTS = "https://api.warframestat.us/pc/alerts"
    ARBITRATION = "https://api.warframestat.us/pc/arbitration"
    INVASIONS = "https://api.warframestat.us/pc/invasions"
    VOID_TRADER = "https://api.warframestat.us/pc/voidTrader"
    EVENTS = "https://api.warframestat.us/pc/events"
    NEWS = "https://api.warframestat.us/pc/news"

    # Daily stuff
    ARCHON_HUNT = "https://api.warframestat.us/pc/archonHunt"
    STEEL_PATH = "https://api.warframestat.us/pc/steelPath"
    SORTIE = "https://api.warframestat.us/pc/sortie"

    # Misc
    CONCLAVE = "https://api.warframestat.us/pc/conclaveChallenges"
    CONSTRUCTION_PROGRESS = "https://api.warframestat.us/pc/constructionProgress"
    EARTH_CYCLE = "https://api.warframestat.us/pc/earthCycle"
    FISSURES = "https://api.warframestat.us/pc/fissures"
    GLOBAL_UPGRADES = "https://api.warframestat.us/pc/globalUpgrades" # don't really know what this is for
    KUVA_MISSIONS = "https://api.warframestat.us/pc/kuva"
    NIGHTWAVE = "https://api.warframestat.us/pc/nightwave"
    PERSISTENT_ENEMIES = "https://api.warframestat.us/pc/persistentEnemies"
    RIVENS = "https://api.warframestat.us/pc/rivens"
    SENTIENT_OUTPOST = "https://api.warframestat.us/pc/sentientOutposts"
    SANCTUARY = "https://api.warframestat.us/pc/simaris"
    SYNDICATE_MISSIONS = "https://api.warframestat.us/pc/syndicateMissions"


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


def build_enpoint(endpoint: Endpoint, language: Language=Language.EN):
    return f"{endpoint.value}/?language={language.value}"