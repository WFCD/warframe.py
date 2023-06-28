# queries are just another way to get the data to the corresponding objects.
# this is really just personal preference.

import asyncio
from typing import Any, Callable, Coroutine

from warframe.worldstate import WorldstateClient
from warframe.worldstate.models import Arbitration, Cetus

client = WorldstateClient()


@client.listen_to(Cetus)
async def on_arbi_state_change(cetus: Cetus) -> None:
    print(cetus)


async def main():
    print((await client.get_cetus()))
    on_arbi_state_change.start()
    while True:
        await asyncio.sleep(2)  # Run the program for 10 minutes


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
