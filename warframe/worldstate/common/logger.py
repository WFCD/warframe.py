from __future__ import annotations

from logging import Logger
from typing import TYPE_CHECKING, Type, Union

if TYPE_CHECKING:
    from ..client import _SingleQueryTimedEvent


__all__ = ["WorldstateLogger"]


class WorldstateLogger(Logger):
    def __init__(self, name: str, level: Union[str, int] = 0) -> None:
        super().__init__(name, level)

    def debug(self, msg: object, *args: object) -> None:
        return super().debug(f"[WorldstateClient DEBUG] {msg}", *args)

    def listener_debug(
        self, msg: object, listener_cls: Type[_SingleQueryTimedEvent], *args: object
    ) -> None:
        return super().debug(
            f"[WorldstateClient DEBUG : listener : {listener_cls}] {msg}", *args
        )
