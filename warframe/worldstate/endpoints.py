from enum import Enum

from .enums import Language

BASE_URL = "https://api.warframestat.us/pc"

__all__ = ["Language"]

# TODO: Slowly remove this enum, remove the corresponding endpoint here as soon as the model is implemented
# or: leave a comment


class Endpoint(Enum):
    # Alert related
    Alert = "/alerts"  # still needs testing

    Event = "/events"
    News = "/news"
    # Daily stuff
    ArchonHunt = "/archonHunt"
    SteelPath = "/steelPath"
    Sortie = "/sortie"

    # Misc
    Conclave = "/conclaveChallenges"
    ConstructionProgress = "/constructionProgress"
    EarthCycle = "/earthCycle"
    GlobalUpgrade = "/globalUpgrades"  # modifiers (like double res weekend)
    KuvaMission = "/kuva"
    Nightwave = "/nightwave"
    PersistentEnemy = "/persistentEnemies"
    Riven = "/rivens"
    SentientOutpost = "/sentientOutposts"
    Sanctuary = "/simaris"
    SyndicateMission = "/syndicateMissions"


def build_endpoint(endpoint: str, language: Language = Language.EN) -> str:
    """Returns an URL based on the endpoint and language

    Args:
        endpoint (str): The endpoint of the request.
        language (Language, optional): The language the API should respond in. Defaults to Language.EN.

    Returns:
        str: The built URL.
    """
    return f"{BASE_URL}{endpoint}/?language={language.value}"
