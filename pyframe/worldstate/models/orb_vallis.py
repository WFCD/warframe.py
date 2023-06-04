from datetime import datetime
from typing import Literal, Optional

from ..common import SingleQueryModel

__all__ = ["OrbVallis"]


class OrbVallis(SingleQueryModel):
    __endpoint__ = "/vallisCycle"

    # required
    expiry: datetime
    time_left: str
    is_warm: bool

    # optional
    activation: Optional[datetime] = None
    state: Optional[Literal["warm", "cold"]] = None
