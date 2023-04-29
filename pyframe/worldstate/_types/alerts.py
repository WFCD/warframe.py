from dataclasses import dataclass
import datetime
from typing import Optional, TypedDict

from typing_extensions import Self

from .base_objects import Record, WorldstateObject, Node, Faction, MissionType

# TODO: IMPLEMENT REWARDS to be another type (https://docs.warframestat.us/#tag/Worldstate/operation/getAlertsByPlatform)


class _AlertMissionRecord(Record, TypedDict):
    reward: ...
    node: str
    nodeKey: str
    faction: Faction
    factionKey: Faction
    maxEnemyLevel: int
    minEnemyLevel: int
    maxWaveNum: int
    type: str
    typeKey: str
    nightmare: bool
    archwingRequired: bool
    isSharkwing: bool
    enemySpec: str
    levelOverride: str
    advancedSpawners: list[str]
    requiredItems: list[str]
    consumeRequiredItems: bool
    leadersAlwaysAllowed: bool
    levelAuras: list[str]
    description: str

@dataclass
class AlertMission(WorldstateObject):
    reward: ...
    location: Node
    faction: Optional[Faction]
    max_enemy_level: int
    min_enemy_level: int
    max_wave: int
    mission_type: Optional[MissionType]
    is_nightmare: bool
    archwing_required: bool
    is_sharkwing: bool
    enemy_spec: str
    level_override: str
    advanced_spawners: list[str]
    required_items: list[str]
    requires_consumable_items: bool
    leaders_always_allowed: bool
    level_auras: list[str]
    description: str

    @classmethod
    def _from_response(cls, response: _AlertMissionRecord) -> Self:
        raise NotImplementedError("Implement reward correctly.")
        return cls(
            reward=response["reward"],
            location=Node(
                node=response["node"],
                node_key=response["nodeKey"]
            ),
            faction=getattr(Faction, response["faction"], None),
            max_enemy_level=response["maxEnemyLevel"],
            min_enemy_level=response["minEnemyLevel"],
            max_wave=response["maxWaveNum"],
            mission_type=getattr(MissionType, response["type"].replace(" ", ""), None),
            is_nightmare=response["nightmare"],
            archwing_required=response["archwingRequired"],
            is_sharkwing=response["isSharkwing"],
            enemy_spec=response["enemySpec"],
            level_override=response["levelOverride"],
            advanced_spawners=response["advancedSpawners"],
            required_items=response["requiredItems"],
            requires_consumable_items=response["consumeRequiredItems"],
            leaders_always_allowed=response["leadersAlwaysAllowed"],
            level_auras=response["levelAuras"],
            description=response["description"]
        )


class _AlertRecord(Record, TypedDict):
    activation: str
    expiry: str
    startString: str
    active: bool
    mission: _AlertMissionRecord
    expired: bool
    eta: str
    rewardTypes: list


@dataclass
class Alert(WorldstateObject):
    activation: datetime.datetime
    expiry: datetime.datetime
    start_string: str
    active: bool
    mission: AlertMission
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
            mission=AlertMission._from_response(response["mission"]),
            expired=response_item['expired'],
            eta=response_item['eta'],
            reward_types=response_item['rewardTypes'],
        )
            for response_item
            in response
        ]
