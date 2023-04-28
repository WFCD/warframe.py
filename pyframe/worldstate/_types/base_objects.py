from abc import ABC, abstractmethod
from typing_extensions import Self


class Record:
    pass


class WorldstateObject(ABC):

    @classmethod
    @abstractmethod
    def _from_response(cls, response: Record) -> Self:
        pass
