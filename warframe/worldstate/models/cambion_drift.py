from typing import Literal

from ..common import SingleQueryModel, TimedEvent

__all__ = ["CambionDrift"]


class CambionDrift(SingleQueryModel, TimedEvent):
    __endpoint__ = "/cambionCycle"

    # required
    state: Literal["vome", "fass"]
    'The state of the Cambion Drift. ("vome" or "fass")'
