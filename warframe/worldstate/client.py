import asyncio
import logging
from datetime import datetime, timezone
from functools import wraps
from typing import (
    Any,
    Callable,
    Coroutine,
    List,
    Optional,
    Type,
    TypeVar,
    Union,
    overload,
)

import aiohttp
import msgspec

from .common import (
    MultiQueryModel,
    SingleQueryModel,
    TimedEvent,
    WorldstateObject,
    _TimedAndSingleQuery,
)
from .endpoints import Language, build_endpoint
from .exceptions import ErrorMessage, SessionNotFound, WorldstateAPIError
from .listeners import TypeListener
from .models import Alert, CambionDrift, Cetus, OrbVallis

__all__ = ["WorldstateClient"]

SupportsSingleQuery = TypeVar("SupportsSingleQuery", bound=SingleQueryModel)
SupportsMultiQuery = TypeVar("SupportsMultiQuery", bound=MultiQueryModel)


T = TypeVar("T", bound=WorldstateObject)


SingleQueryTimedEvent = TypeVar("SingleQueryTimedEvent", bound=_TimedAndSingleQuery)


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
        """
        Parameters
        ----------
        session : Optional[aiohttp.ClientSession], optional
            The `aiohttp.ClientSession` the client will perform the requests on, by default None
        default_language : Language, optional
            The default language the objects will be in, by default `Language.EN`
        logger : Optional[WorldstateLogger], optional
            The logger that will log messages, by default None
        """
        self._session = session
        self._session_created = False

        self._default_lang = default_language
        self._listeners: List[TypeListener] = []

    #
    # Request
    #

    async def _request(
        self,
        type: Type[Union[SingleQueryModel, MultiQueryModel]],
        language: Optional[Language],
    ) -> str:
        """
        Sends a request to the given `endpoint` and returns its JSON content as string.

        Parameters
        ----------
        endpoint : str
            The endpoint to send the request to.
        language : Optional[Language], optional
            The language of the response, by default None

        Raises
        ------
        SessionNotFound
            When the client's session is gone / None for some reason.
        WorldstateAPIError
            When the API returns a faulty response.

        Returns
        -------
        str
            The JSON content as string.
        """

        if not self._session:
            self._session = aiohttp.ClientSession()
            self._session_created = True

        if self._session.closed:
            raise SessionNotFound("The WorldstateClient's session is closed.")

        language = language or self._default_lang

        url = build_endpoint(type, language)

        logging.getLogger(__name__).debug(
            f"Sending request to the {type.__name__} endpoint"
        )

        async with self._session.get(url) as response:
            response_text = await response.text()

            if response.status != 200:
                raise WorldstateAPIError(
                    msgspec.json.decode(response_text, type=ErrorMessage)
                )

            logging.getLogger(__name__).debug(
                f"Got request from the {type.__name__} endpoint"
            )

            return response_text

    #
    # Queries
    #

    @overload
    async def query(
        self,
        cls: Type[SupportsSingleQuery],
        language: Optional[Language] = None,
    ) -> SupportsSingleQuery:
        """
        Queries the model of type `SingleQueryModel` to return its corresponding object.

        Parameters
        ----------
        cls : Type[SupportsSingleQuery]
            The model to query.
        language : Optional[Language], optional
            The language to return the queried model in, by default None

        Returns
        -------
        SupportsSingleQuery
            The queried model.
        """
        ...

    @overload
    async def query(
        self,
        cls: Type[SupportsMultiQuery],
        language: Optional[Language] = None,
    ) -> List[SupportsMultiQuery]:
        """
        Queries the model of type `MultiQueryModel` to return a list of its corresponding object.

        Parameters
        ----------
        cls : Type[SupportsMultiQuery]
            The model to query.
        language : Optional[Language], optional
            The language to return the queried model in, by default None

        Returns
        -------
        List[SupportsMultiQuery]
            A list of the queried model.
        """
        ...

    async def query(
        self,
        cls: Type[Union[SupportsSingleQuery, SupportsMultiQuery]],
        language: Optional[Language] = None,
    ) -> Union[SupportsSingleQuery, List[SupportsMultiQuery]]:
        # -----
        json = await self._request(cls, language)
        return cls._from_json(json)

    async def query_list_of(
        self, cls: Type[SupportsMultiQuery], language: Optional[Language] = None
    ) -> List[SupportsMultiQuery]:
        """
        Queries the model of type `MultiQueryModel` to return its corresponding object.

        Parameters
        ----------
        cls : Type[SupportsSingleQuery]
            The model to query.
        language : Optional[Language], optional
            The language to return the object in, by default None.

        Raises
        ------
        UnsupportedSingleQueryError
            When the passed type `cls` is not a subclass of `SingleQueryModel`.

        Returns
        -------
        Optional[List[SupportsMultiQuery]]
            A list of the queried model.
        """
        logging.getLogger(__name__).warn(
            "Deprecation warning: `query_list_of(type)` is deprecated and will be removed in version 2.0. Use `query(type)` instead."
        )
        json = await self._request(cls, language)
        return cls._from_json(json)

    #
    # Type-Specific commands
    #

    async def get_cetus(self, language: Optional[Language] = None) -> Cetus:
        json = await self._request(Cetus, language)
        return Cetus._from_json(json)

    async def get_cambion_drift(
        self, language: Optional[Language] = None
    ) -> CambionDrift:
        json = await self._request(CambionDrift, language)
        return CambionDrift._from_json(json)

    async def get_orb_vallis(self, language: Optional[Language] = None) -> OrbVallis:
        json = await self._request(OrbVallis, language)
        return OrbVallis._from_json(json)

    async def get_alerts(
        self, language: Optional[Language] = None
    ) -> Optional[List[Alert]]:
        json = await self._request(OrbVallis, language)
        return Alert._from_json(json)

    #
    # Event-hook related
    #

    def register_listener(self, listener: TypeListener):
        """
        Registers an event listener.

        Parameters
        ----------
        listener : _TaskHelper
            The listener you want to register.
        """
        logging.getLogger(__name__ + "_listeners").debug(
            f"Registered a listener of type {listener._type.__name__}"
        )
        self._listeners.append(listener)

    def listen_to(self, type: Type[SingleQueryTimedEvent]):
        """A decorator that makes a function an event listener. This will trigger on state changes (e.g. on Cetus: Day -> Night / Night -> Day)

        Args:
            type (Type[SingleQueryTimedEvent]): Any type that inherits SingleQueryObject and TimedEvent

        Raises:
            TypeError: If the type requirements are not met

        Returns:
            _TaskHelper: A helper class that wraps the callback function. Call `.start()` on it in order to start the listener. Same goes for `.stop()`
        """
        if not issubclass(type, SingleQueryModel) and not not issubclass(
            type, TimedEvent
        ):
            raise TypeError(
                f"{type.__name__} has to implement SingleQueryModel and TimedEvent"
            )

        def decorator(
            func: Callable[[SingleQueryTimedEvent], Coroutine[Any, Any, None]]
        ) -> TypeListener:
            @wraps(func)
            async def inner() -> None:
                item: SingleQueryTimedEvent = await self.query(type)  # type: ignore
                while True:
                    try:
                        # check if the event is over, if so, retry in 1 minute (API doesn't refresh at the exact point of expiry)
                        if item.expiry <= datetime.now(tz=timezone.utc):
                            logging.getLogger(__name__ + "_listeners").debug(
                                f"{type.__name__} :: Looking for state change from the API"
                            )

                            await asyncio.sleep(60)

                            new_item: SingleQueryTimedEvent = await self.query(type)  # type: ignore

                            if not item.expiry < new_item.expiry:
                                continue

                            else:
                                # we now know that it is a different event, so we can call the callback function
                                # with the new item after the last one's expiry
                                await func(new_item)

                                # we called the function, so we need to update the "last used item"
                                item = new_item

                        # calculate seconds until next event triggers
                        seconds_to_wait = (
                            item.expiry - datetime.now(tz=timezone.utc)
                        ).total_seconds()

                        if seconds_to_wait > 0:
                            logging.getLogger(__name__ + "_listeners").debug(
                                f"{type.__name__} :: Sleeping {seconds_to_wait} seconds"
                            )
                        await asyncio.sleep(
                            seconds_to_wait
                            + 1  # to avoid slight offsets resulting in this part being called a ton of times
                        )

                    except asyncio.CancelledError:
                        break

            t_helper = TypeListener(inner, type)
            self.register_listener(t_helper)
            return t_helper

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
