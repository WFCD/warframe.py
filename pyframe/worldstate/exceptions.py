__all__ = [
    "WorldstateAPIError"
]

class WorldstateAPIError(Exception):
    def __init__(self, message: str, *args: object) -> None:
        super().__init__(*args)
        self.message = message