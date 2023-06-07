# queries are just another way to get the data to the corresponding objects.
# this is really just personal preference.

import asyncio

from warframe.worldstate import WorldstateClient
from warframe.worldstate.models import Arbitration


async def main():
    async with WorldstateClient() as client:
        # import from models and pass the type you want the object of
        arbi = await client.query(Arbitration)

        print(arbi)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
