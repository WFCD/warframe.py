# queries are just another way to get the data to the corresponding objects.
# this is really just personal preference.

import asyncio

from warframe.worldstate import WorldstateClient
from warframe.worldstate.models import Arbitration, Fissure


async def main():
    async with WorldstateClient() as client:
        # import from models and pass the type you want the object of
        arbi = await client.query(Arbitration)  # of Type SingleQuery - a single  object  of type `Arbitration`
        fissures = await client.query(Fissure)  # of Type MultiQuery  - a list of objects of type `Fissure`

        print(arbi)
        for fissure in fissures:
            print(fissure)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
