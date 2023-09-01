from enum import Enum
from typing import Type, Union

from .common.core import MultiQueryModel, SingleQueryModel
from .enums import Language

BASE_URL = "https://api.warframestat.us/pc"

__all__ = ["Language"]

# TODO: Slowly remove this enum, remove the corresponding endpoint here as soon as the model is implemented
# or: leave a comment


class Endpoint(Enum):
    # Alert related
    Alert = "/alerts"  # still needs testing
    Event = "/events"  # incomplete, needs testing

    News = "/news"

    ArchonHunt = "/archonHunt"
    SteelPath = "/steelPath"

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


def build_endpoint(
    type: Type[Union[SingleQueryModel, MultiQueryModel]],
    language: Language = Language.EN,
) -> str:
    """
    Returns an URL based on the endpoint and language.

    Parameters
    ----------
    endpoint : str
        The endpoint of the request.
    language : Language, optional
        The language the API should respond in, by default Language.EN.

    Returns
    -------
    str
        The built URL.
    """

    return f"{BASE_URL}{type.__endpoint__}/?language={language.value}"
