from logging import Logger
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    # as soon as state listeners are merged
    # from ..client import _SingleQueryTimedEvent
    pass

__all__ = ["WorldstateLogger"]


class WorldstateLogger(Logger):
    def __init__(self, name: str, level: Union[str, int] = 0) -> None:
        super().__init__(name, level)

    def debug(self, msg: object, *args: object) -> None:
        return super().debug(f"[WorldstateClient DEBUG] {msg}", *args)

    # def listener_debug(
    #         self,
    #         msg: object,
    #         *args: object,
    #         listener_cls: Type[_SingleQueryTimedEvent]
    # ) -> None:
    #     return super().debug(
    #         f"[WorldstateClient DEBUG : listener : {listener_cls}] {msg}",
    #         *args
    #     )
