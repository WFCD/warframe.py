import asyncio
from abc import ABC, abstractmethod
from typing import Any, Callable, Coroutine, Optional, Type

from .common.types_ import _TimedAndSingleQuery


class Listener(ABC):
    def __init__(self, func: Callable[[], Coroutine[Any, Any, None]]) -> None:
        self.func = func

    @abstractmethod
    def start(self):
        raise NotImplementedError()

    @abstractmethod
    def stop(self):
        raise NotImplementedError()


class TypeListener(Listener):
    def __init__(
        self,
        func: Callable[[], Coroutine[Any, Any, None]],
        type: Type[_TimedAndSingleQuery],
    ) -> None:
        self._task: Optional[asyncio.Task] = None
        self._type = type
        super().__init__(func)

    def start(self) -> None:
        if self._task is None:
            self._task = asyncio.create_task(self.func())

    def stop(self) -> None:
        if self._task:
            self._task.cancel()
            self._task = None
