import asyncio

from warframe.worldstate import Language, WorldstateClient


async def main():
    async with WorldstateClient() as client:
        cetus = await client.get_cetus(language=Language.English)  # english is default
        print(cetus.short_string)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
