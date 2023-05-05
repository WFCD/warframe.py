# pyframe

An asynchronous Python API wrapper for [the Warframestat API](https://hub.warframestat.us) and (later) [the warframe.market API](https://warframe.market/api_docs).

# What to expect

This library is in its *very* early states. I am willing to spend a long time on this project to make it the best and most up-to-date Python Warframe API wrapper.

# Quickstart
```py
import asyncio

from pyframe import WorldstateClient, Language


async def main():
    async with WorldstateClient() as client:
        cetus = await client.get_cetus(language=Language.English) # english is default
        print(cetus.__dict__)



if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
    ```
