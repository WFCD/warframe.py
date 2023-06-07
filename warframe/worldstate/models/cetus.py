from datetime import datetime
from typing import Literal, Optional

from ..common import SingleQueryModel

__all__ = ["Cetus"]


class Cetus(SingleQueryModel):
    __endpoint__ = "/cetusCycle"

    # required
    expiry: datetime
    is_day: bool
    time_left: str

    # optional
    activation: Optional[datetime] = None
    start_string: Optional[str] = None
    active: Optional[bool] = None
    state: Optional[Literal["day", "night"]] = None
    short_string: Optional[str] = None
