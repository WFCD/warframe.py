import asyncio
from typing import Literal

from warframe.worldstate import WorldstateClient
from warframe.worldstate.common.core import SingleQueryModel, TimedEvent  # this import might change


class CustomCambionDrift(SingleQueryModel, TimedEvent):
    """
    This "feature" is there to provide an option to implement something that is not yet implemented.

    Short explanation:
    The Cambion Drift's endpoint responds in a single (json) object that's why we give it `SingleQueryModel`.
    It is also a `TimedEvent` because it has an activation, expiry, etc. (basically a cycle).

    Now, to add the attributes to the class simply look at the API docs.
    Note that existing names will be converted from `camelCase` to `snake_case`.
    To rename a given key (from the API response) simply use `msgspec.field` and set the `name` to its original, snake_case'd name.
    e.g.:
    ```py
        my_renamed_state: Literal["vome", "fass"] = msgspec.field(name="state")
    ```

    `https://api.warframestat.us/pc` will be concatenated with `__endpoint__`.

    After that's all done, simply slap your own Model into `client.query` and let warframe.py do its magic :)
    """

    __endpoint__ = "/cambionCycle"  # specify endpoint here

    state: Literal["vome", "fass"]


async def main():
    async with WorldstateClient() as client:
        ccd = await client.query(CustomCambionDrift)

        print(ccd)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
