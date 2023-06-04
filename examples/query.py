# queries are just another way to get the data to the corresponding objects.
# this is really just personal preference.

import asyncio

from pyframe.worldstate import WorldstateClient
from pyframe.worldstate.models import Arbitration


# to use a custom session for the client, use the following:
async def main():
    async with WorldstateClient() as client:
        arbi = await client.query(Arbitration)

        print(arbi)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
