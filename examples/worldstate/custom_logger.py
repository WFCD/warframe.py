import asyncio
import logging

from warframe.worldstate import WorldstateClient, WorldstateLogger
from warframe.worldstate.models import Cetus


async def main():
    # Note that the default logger is pretty much empty (nothing will be logged)
    # so if you want to make use of the logger, make your own:
    logger = WorldstateLogger("name whatever you want", logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    async with WorldstateClient(logger=logger) as client:  # pass the logger
        cetus = await client.query(Cetus)

        print(cetus)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
