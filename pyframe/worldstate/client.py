import aiohttp

from ._types import CambionDrift, Cetus, OrbVallis


class PyframeClient:
    def __init__(self, session: aiohttp.ClientSession = None) -> None:
        self._session = session
        self._session_created = False

    async def get_cetus():
        raise NotImplementedError()



    async def __aenter__(self) -> 'PyframeClient':
        if not self._session:
            self._session = aiohttp.ClientSession()
            self._session_created = True

        return self
    
    async def __aexit__(self, exc_type, exception, traceback):
        if self._session_created:
            await self._session.close()
