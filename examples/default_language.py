import asyncio

from pyframe.worldstate import Language, WorldstateClient
from pyframe.worldstate.models import Arbitration


async def main():
    async with WorldstateClient(
        default_language=Language.ZH  # set the default language to chinese here
    ) as client:
        arbi_zh = await client.query(Arbitration)
        print(arbi_zh)

        arbi_en = await client.query(
            Arbitration, language=Language.EN
        )  # you can still override it manually here
        print(arbi_en)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
