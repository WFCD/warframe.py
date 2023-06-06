# pyframe

An asynchronous Python API wrapper for [the Warframestat API](https://hub.warframestat.us) and (later) [the warframe.market API](https://warframe.market/api_docs).

# What to expect

This library is in its early states. I am willing to spend a long time on this project to make it the best and most up-to-date Python Warframe API wrapper.

# Quickstart
```py
import asyncio

from pyframe.worldstate import Language, WorldstateClient


async def main():
    async with WorldstateClient() as client:
        cetus = await client.get_cetus(language=Language.English)  # english is default
        print(cetus.short_string)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())

```

# Installing

`pip install git+https://github.com/Mettwasser/pyframe.git`

Supported python versions:
- 3.11
- 3.10
- 3.9
