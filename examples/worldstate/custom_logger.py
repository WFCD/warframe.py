import asyncio
import logging

from warframe.worldstate import WorldstateClient, utils
from warframe.worldstate.models import Cetus


async def main():
    # Note that the default logger is pretty much empty (nothing will be logged)
    # so if you want to make use of the logger, you can use this helper function:
    utils.setup_logging(handler=logging.StreamHandler(), level=logging.DEBUG, root=True)

    async with WorldstateClient() as client:
        cetus = await client.query(Cetus)

        print(cetus)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
