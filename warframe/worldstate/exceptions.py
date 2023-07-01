from typing import TypeVar

from msgspec import field

from .common import WorldstateObject

__all__ = [
    "WorldstateAPIError",
    "WorldstateError",
]

T = TypeVar("T")


class ErrorMessage(WorldstateObject):
    message: str = field(name="error")
    code: int


class WorldstateError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class WorldstateAPIError(WorldstateError):
    def __init__(self, error_message: ErrorMessage, *args) -> None:
        super().__init__(*args)
        self.error_message: ErrorMessage = error_message


class SessionNotFound(WorldstateError):
    pass
