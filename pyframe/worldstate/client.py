from typing import Coroutine

import aiohttp

from .reponse_models import CambionDrift, Cetus, OrbVallis
from .endpoints import Endpoint, Language, build_endpoint
from .exceptions import WorldstateAPIError

__all__ = ["WorldstateClient"]


class WorldstateClient:
    """
    The Pyframe Client for the worldstate API.
    Instantiate with an asynchronous context managaer.
    """

    def __init__(self, session: aiohttp.ClientSession = None) -> None:
        self._session = session
        self._session_created = False

        self._debug = False

    async def _request(self, endpoint: Endpoint, language: Language) -> dict:
        endpoint = build_endpoint(endpoint, language)

        if self._debug:
            print(f"[WorldstateClient DEBUG] Sending request to {endpoint}...")

        async with self._session.get(endpoint) as response:
            response_body = await response.json()

            if response.status != 200:
                raise WorldstateAPIError(response_body["error"])

            if self._debug:
                print(f"[WorldstateClient DEBUG] Got request:\n{response_body}")

            return response_body

    async def get_cetus(self, language: Language = Language.EN) -> Cetus:
        json = await self._request(Endpoint.CETUS, language)
        return Cetus._from_response(json)

    async def get_cambion_drift(self, language: Language = Language.EN) -> CambionDrift:
        json = await self._request(Endpoint.CAMBION_DRIFT, language)
        return CambionDrift._from_response(json)

    async def get_orb_vallis(self, language: Language = Language.EN) -> OrbVallis:
        json = await self._request(Endpoint.ORB_VALLIS, language)
        return OrbVallis._from_response(json)

    async def __aenter__(self) -> "WorldstateClient":
        if not self._session:
            self._session = aiohttp.ClientSession()
            self._session_created = True

        return self

    async def __aexit__(self, exc_type, exception, traceback):
        if self._session_created:
            await self._session.close()
