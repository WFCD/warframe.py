import asyncio
from datetime import datetime
from functools import wraps
from typing import (
    Any,
    Callable,
    Coroutine,
    List,
    NamedTuple,
    Optional,
    Type,
    TypeVar,
    Union,
)

import aiohttp
import msgspec

from .common import MultiQueryModel, SingleQueryModel, TimedEvent
from .endpoints import Language, build_endpoint
from .exceptions import (
    ErrorMessage,
    SessionNotFound,
    UnsupportedMultiQueryError,
    UnsupportedSingleQueryError,
    UnsupportedTypeError,
    WorldstateAPIError,
)
from .models import Alert, CambionDrift, Cetus, OrbVallis

__all__ = ["WorldstateClient"]

SupportsSingleQuery = TypeVar("SupportsSingleQuery", bound=SingleQueryModel)
SupportsMultiQuery = TypeVar("SupportsMultiQuery", bound=MultiQueryModel)

IsTimed = TypeVar("IsTimed", bound=TimedEvent)


class _TaskHelper:
    def __init__(self, loop: Callable[..., Coroutine[Any, Any, None]]) -> None:
        self._loop = loop
        self._task: Optional[asyncio.Task] = None

    def start(self) -> None:
        if self._task is None:
            self._task = asyncio.ensure_future(self._loop())

    def stop(self) -> None:
        if self._task:
            self._task.cancel()


class _TriggerContext(NamedTuple):
    seconds: int
    timedevent: Type[TimedEvent]


class WorldstateClient:
    """
    The warframe.py Client for the worldstate API.
    Instantiate with an asynchronous context manager or by simply creating an instance.
    Note that the close method for the client is a coroutine.
    """

    def __init__(
        self,
        *,
        session: Optional[aiohttp.ClientSession] = None,
        default_language: Language = Language.EN,
    ) -> None:
        self._session = session
        self._session_created = False

        self._default_lang = default_language

        self._debug = True

    #
    # Request
    #

    async def _request(self, endpoint: str, language: Optional[Language]) -> str:
        """Sends a request to the given `endpoint` and returns its JSON content as string.

        Args:
            endpoint (str): The endpoint to send the request to.
            language (Optional[Language]): The language of the response.

        Raises:
            SessionNotFound: When the client's session is gone / None for some reason.
            WorldstateAPIError: When the API returns a faulty response.

        Returns:
            str: The JSON content as string.
        """
        if not self._session:
            self._session = aiohttp.ClientSession()
            self._session_created = True

        if self._session.closed:
            raise SessionNotFound("The WorldstateClient's session is closed.")

        language = language or self._default_lang

        url = build_endpoint(endpoint, language)

        if self._debug:
            print(f"[WorldstateClient DEBUG] Sending request to {url}...")

        async with self._session.get(url) as response:
            response_text = await response.text()

            if response.status != 200:
                raise WorldstateAPIError(
                    msgspec.json.decode(response_text, type=ErrorMessage)
                )

            if self._debug:
                print(f"[WorldstateClient DEBUG] Got request:\n{response_text}")

            return response_text

    #
    # Queries
    #

    async def query(
        self, cls: Type[SupportsSingleQuery], language: Optional[Language] = None
    ) -> SupportsSingleQuery:
        """Queries the model of type `SingleQueryModel` to return its corresponding object.

        Args:
            cls (Type[SupportsSingleQuery]): The model to query.
            language (Optional[Language], optional): The language to return the object in. Defaults to None.

        Raises:
            UnsupportedSingleQueryError: When the passed type `cls` is not a subclass of `SingleQueryModel`.

        Returns:
            SupportsSingleQuery: The queried model.
        """
        if not issubclass(cls, SingleQueryModel):
            raise UnsupportedSingleQueryError(
                f"{cls.__name__} is required to be of type SingleQueryModel."
            )
        json = await self._request(cls.__endpoint__, language)

        return cls._from_json(json)

    async def query_list_of(
        self, cls: Type[SupportsMultiQuery], language: Optional[Language] = None
    ) -> List[SupportsMultiQuery]:
        """Queries the model of type `MultiQueryModel` to return its corresponding object.

        Args:
            cls (Type[SupportsSingleQuery]): The model to query.
            language (Optional[Language], optional): The language to return the object in. Defaults to None.

        Raises:
            UnsupportedSingleQueryError: When the passed type `cls` is not a subclass of `SingleQueryModel`.

        Returns:
            Optional[List[SupportsMultiQuery]]: A list of the queried model.
        """
        if not issubclass(cls, MultiQueryModel):
            raise UnsupportedMultiQueryError(
                f"{cls.__name__} is required to be of type MultiQueryModel."
            )
        json = await self._request(cls.__endpoint__, language)

        return cls._from_json(json)

    #
    # Type-Specific commands
    #

    async def get_cetus(self, language: Optional[Language] = None) -> Cetus:
        json = await self._request(Cetus.__endpoint__, language)
        return Cetus._from_json(json)

    async def get_cambion_drift(
        self, language: Optional[Language] = None
    ) -> CambionDrift:
        json = await self._request(CambionDrift.__endpoint__, language)
        return CambionDrift._from_json(json)

    async def get_orb_vallis(self, language: Optional[Language] = None) -> OrbVallis:
        json = await self._request(OrbVallis.__endpoint__, language)
        return OrbVallis._from_json(json)

    async def get_alerts(
        self, language: Optional[Language] = None
    ) -> Optional[List[Alert]]:
        json = await self._request(OrbVallis.__endpoint__, language)
        return Alert._from_json(json)

    #
    # Event-hook related
    #

    async def _get_next_trigger(self, type: Type[IsTimed]) -> _TriggerContext:
        item: Type[TimedEvent] = await self.query(
            type  # type: ignore
        )  # needs to be here, else it wont accept the type. This us guaranteed to be, cause of the check in the decorator
        return _TriggerContext((datetime.now() - item.expiry).seconds, item)

    def listen_to(self, type: Type[IsTimed]):
        if not issubclass(type, SingleQueryModel) and not issubclass(type, TimedEvent):
            raise UnsupportedTypeError(
                f"{type.__name__} has to implement SingleQueryModel and TimedEvent"
            )

        def decorator(func: Callable[..., Coroutine[Any, Any, None]]) -> _TaskHelper:
            @wraps(func)
            async def inner() -> None:
                while True:
                    is_retrying = False
                    try:
                        seconds, item = await self._get_next_trigger(type)
                        # check if the event is over, if so, retry in 1 minute
                        if seconds <= 0:
                            seconds = 60
                            is_retrying = True
                            if self._debug:
                                print(
                                    f"[WorldstateClient DEBUG : listener : {type}] Retry started. Looking for state change from the API"
                                )

                        if self._debug:
                            print(
                                f"[WorldstateClient DEBUG : listener : {type}] Sleeping {seconds} seconds"
                            )
                        await asyncio.sleep(seconds)

                        if not is_retrying:
                            await func(item)

                    except asyncio.CancelledError:
                        break

            return _TaskHelper(inner)

        return decorator

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

    #
    # Closing the client
    #

    async def close(self):
        if self._session and self._session_created:
            await self._session.close()
