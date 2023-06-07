import asyncio

import aiohttp  # comes with this package

from warframe.worldstate import Language, WorldstateClient


# to use a custom session for the client, use the following:
async def main():
    async with aiohttp.ClientSession() as session:
        # pass `session` to WorldstateClient
        async with WorldstateClient(session=session) as client:
            cetus = await client.get_cetus(language=Language.English)
            print(cetus.activation, cetus.is_day)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
