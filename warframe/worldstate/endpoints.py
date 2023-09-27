from __future__ import annotations

import urllib.parse as urlparse
from typing import Dict, List, Tuple, Type, Union

from .common.core import MultiQueryModel, SingleQueryModel
from .enums import Language

BASE_URL = "https://api.warframestat.us"

__all__ = ["by_type", "by_query"]


def by_type(
    type: Type[Union[SingleQueryModel, MultiQueryModel]],
    language: Language = Language.EN,
) -> str:
    """
    Returns an URL based on the endpoint and language.

    Parameters
    ----------
    type : Type[Union[SingleQueryModel, MultiQueryModel]]
        The type.
    language : Language, optional
        The language the API should respond in, by default Language.EN.

    Returns
    -------
    str
        The built URL.
    """

    return f"{BASE_URL}/pc{type.__endpoint__}?{urlparse.urlencode({'language': language.value})}"


def by_query(
    query: str,
    language: Language = Language.EN,
    only: str = "",
    remove: str = "",
    by: str = "",
):
    params = {"language": language.value}

    if only:
        params["only"] = only

    elif remove:
        params["remove"] = remove

    if by:
        params["by"] = by

    return f"{BASE_URL}/items/{urlparse.quote(query)}?{urlparse.urlencode(params)}"
