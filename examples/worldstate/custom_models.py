import asyncio
from datetime import datetime
from typing import Literal, Optional

from msgspec import field  # use this to rename response keys

from warframe.worldstate import WorldstateClient
from warframe.worldstate.common.base_objects import (
    SingleQueryModel,
)  # this import might change


class CustomCambionDrift(SingleQueryModel):
    __endpoint__ = "/cambionCycle"  # specify endpoint here

    # required

    # at the endpoint, it is called expiry, to rename it use this:
    expiry_dt: datetime = field(name="expiry")

    activation: datetime
    state: Literal["vome", "fass"]

    # optional

    # to rename with default values, use this:
    time_remaining: Optional[str] = field(name="timeLeft", default=None)


async def main():
    async with WorldstateClient() as client:
        arbi = await client.query(CustomCambionDrift)

        print(arbi)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
