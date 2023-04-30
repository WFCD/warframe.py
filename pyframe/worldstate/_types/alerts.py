from dataclasses import dataclass
import datetime
from typing import Optional

from typing_extensions import Self

from .base import Record, WorldstateObject, StarchartNode, Faction, MissionType

# TODO: IMPLEMENT REWARDS to be another type (https://docs.warframestat.us/#tag/Worldstate/operation/getAlertsByPlatform)


class _AlertMissionRecord(Record):
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


@dataclass(frozen=True, order=True)
class AlertMission(WorldstateObject):
    reward: ...
    location: StarchartNode
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
            reward=response.get("reward"),
            location=StarchartNode(
                node=response.get("node"), node_key=response.get("nodeKey")
            ),
            faction=getattr(Faction, response.get("faction"), None),
            max_enemy_level=response.get("maxEnemyLevel"),
            min_enemy_level=response.get("minEnemyLevel"),
            max_wave=response.get("maxWaveNum"),
            mission_type=getattr(MissionType, response["type"].replace(" ", ""), None),
            is_nightmare=response.get("nightmare"),
            archwing_required=response.get("archwingRequired"),
            is_sharkwing=response.get("isSharkwing"),
            enemy_spec=response.get("enemySpec"),
            level_override=response.get("levelOverride"),
            advanced_spawners=response.get("advancedSpawners"),
            required_items=response.get("requiredItems"),
            requires_consumable_items=response.get("consumeRequiredItems"),
            leaders_always_allowed=response.get("leadersAlwaysAllowed"),
            level_auras=response.get("levelAuras"),
            description=response.get("description"),
        )


class _AlertRecord(Record):
    # required
    mission: _AlertMissionRecord
    expired: bool
    rewardTypes: list[str]

    # optional
    activation: str
    expiry: str
    startString: str
    active: bool
    eta: str


@dataclass(frozen=True, order=True)
class Alert(WorldstateObject):
    # required
    mission: AlertMission
    expired: bool
    reward_types: list[str]

    # optional
    activation: Optional[datetime.datetime]
    expiry: Optional[datetime.datetime]
    start_string: Optional[str]
    active: Optional[bool]
    eta: Optional[str]

    @classmethod
    def _from_response(cls, response: list[_AlertRecord]) -> list[Self]:
        return [
            cls(
                activation=datetime.datetime.fromisoformat(
                    response_item.get("activation")
                )
                if "activation" in response_item
                else None,
                expiry=datetime.datetime.fromisoformat(response_item.get("expiry"))
                if "expiry" in response_item
                else None,
                start_string=response_item.get("startString"),
                active=response_item.get("active"),
                mission=AlertMission._from_response(response_item.get("mission")),
                expired=response_item.get("expired"),
                eta=response_item.get("eta"),
                reward_types=response_item.get("rewardTypes"),
            )
            for response_item in response
        ]
