from dataclasses import dataclass
from abc import ABC
from datetime import datetime
from typing import Type, TypeVar, Optional, Any, Dict
from typing_extensions import Self

from dacite import Config, from_dict

T = TypeVar("T")


def _from_worldstate_date_str(date_str: str) -> datetime:
    return datetime.fromisoformat(date_str.strip("Z"))


class WorldstateObject(ABC):
    @classmethod
    def _from_response(
        cls: Type[T], response: Dict[str, Any], config: Optional[Config] = None
    ) -> Self:
        config = config or Config()
        if datetime not in config.type_hooks.keys():
            config.type_hooks[datetime] = _from_worldstate_date_str
        return from_dict(data_class=cls, data=response, config=config)


import json


@dataclass(frozen=True, order=True)
class DailyDeal(WorldstateObject):
    # required
    sold: int
    item: str
    total: int
    eta: str
    originalPrice: int
    salePrice: int
    discount: int
    expiry: datetime

    # optional
    activation: Optional[datetime]


d = json.loads(
    r"""
{"item":"Bronco","expiry":"2023-05-30T21:00:00.000Z","activation":"2023-05-29T19:00:00.000Z","originalPrice":190,"salePrice":133,"total":200,"sold":13,"id":"HandShotGun1685480400000","eta":"3h 30m 4s","discount":30}
"""
)

fs = DailyDeal._from_response(d)
print(fs)
