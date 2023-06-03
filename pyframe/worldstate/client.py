from typing import List, Optional, Type, TypeVar

import aiohttp

from .common import SupportsMany, SupportsSingle, WorldstateObject
from .endpoints import Endpoint, Language, build_endpoint, endpoint_from_type
from .exceptions import (
    ErrorMessage,
    UnsupportedManyError,
    UnsupportedSingleError,
    WorldstateAPIError,
)
from .models import CambionDrift, Cetus, OrbVallis, Alert

__all__ = ["WorldstateClient"]

W = TypeVar("W", bound=WorldstateObject)


class WorldstateClient:
    """
    The Pyframe Client for the worldstate API.
    Instantiate with an asynchronous context manager.
    """

    def __init__(self, *, session: Optional[aiohttp.ClientSession] = None) -> None:
        self._session = session
        self._session_created = False

        self._debug = False

    #
    # Request
    #

    async def _request(self, endpoint: Endpoint, language: Language) -> str:
        if not self._session:
            raise NotImplementedError

        url = build_endpoint(endpoint, language)

        if self._debug:
            print(f"[WorldstateClient DEBUG] Sending request to {url}...")

        async with self._session.get(url) as response:
            response_text = await response.text()

            if response.status != 200:
                raise WorldstateAPIError(ErrorMessage._from_json(response_text))

            if self._debug:
                print(f"[WorldstateClient DEBUG] Got request:\n{response_text}")

            return response_text

    #
    # Queries
    #

    async def query(self, cls: Type[W], language: Language = Language.EN) -> W:
        if not issubclass(cls, (WorldstateObject, SupportsSingle)):
            raise UnsupportedSingleError(
                f"{cls.__name__} is required to be of type WorldstateObject and SupportsSingle."
            )
        endpoint = endpoint_from_type(cls)
        json = await self._request(endpoint, language)

        return cls._from_json(json)

    async def query_many(
        self, cls: Type[W], language: Language = Language.EN
    ) -> Optional[List[W]]:
        if not issubclass(cls, (WorldstateObject, SupportsMany)):
            raise UnsupportedManyError(
                f"{cls.__name__} is required to be of type WorldstateObject and SupportsMany."
            )
        endpoint = endpoint_from_type(cls)
        json = await self._request(endpoint, language)

        return cls._many_from_json(json)

    #
    # Type-Specific commands
    #

    async def get_cetus(self, language: Language = Language.EN) -> Cetus:
        json = await self._request(Endpoint.Cetus, language)
        return Cetus._from_json(json)

    async def get_cambion_drift(self, language: Language = Language.EN) -> CambionDrift:
        json = await self._request(Endpoint.CambionDrift, language)
        return CambionDrift._from_json(json)

    async def get_orb_vallis(self, language: Language = Language.EN) -> OrbVallis:
        json = await self._request(Endpoint.OrbVallis, language)
        return OrbVallis._from_json(json)

    async def get_alerts(
        self, language: Language = Language.EN
    ) -> Optional[List[Alert]]:
        json = await self._request(Endpoint.Alert, language)
        return Alert._many_from_json(json)

    #
    # Context manager
    #

    async def __aenter__(self) -> "WorldstateClient":
        if not self._session:
            self._session = aiohttp.ClientSession()
            self._session_created = True

        return self

    async def __aexit__(self, exc_type, exception, traceback):
        if self._session and self._session_created:
            await self._session.close()
