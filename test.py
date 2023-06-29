import asyncio
from typing import Any, Callable, Coroutine

from warframe.worldstate import WorldstateClient
from warframe.worldstate.models import Arbitration, Cetus

client = WorldstateClient()


@client.listen_to(Cetus)
async def on_arbi_state_change(cetus: Cetus) -> None:
    print(cetus)


async def main():
    on_arbi_state_change.start()
    await asyncio.sleep(600)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
