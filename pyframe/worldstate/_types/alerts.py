from dataclasses import dataclass
import datetime
from typing import TypedDict

from typing_extensions import Self

from .base_objects import Record, WorldstateObject

# TODO: Implement the full alert with the sub category mission (https://docs.warframestat.us/#tag/Worldstate/operation/getAlertsByPlatform)

class _AlertRecord(Record, TypedDict):
    activation: str
    expiry: str
    startString: str
    active: bool
    mission: dict
    expired: bool
    eta: str
    rewardTypes: list


@dataclass
class Alert(WorldstateObject):
    activation: datetime.datetime
    expiry: datetime.datetime
    start_string: str
    active: bool
    mission: dict
    expired: bool
    eta: str
    reward_types: list

    @classmethod
    def _from_response(cls, response: list[_AlertRecord]) -> list[Self]:
        return [cls(
            activation=datetime.datetime.fromisoformat(response_item['activation']),
            expiry=response_item['expiry'],
            start_string=response_item['startString'],
            active=response_item['active'],
            mission=response_item['mission'],
            expired=response_item['expired'],
            eta=response_item['eta'],
            reward_types=response_item['rewardTypes'],
        )
            for response_item
            in response
        ]
