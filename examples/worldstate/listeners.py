import asyncio
from typing import Any, Callable, Coroutine

from warframe.worldstate import WorldstateClient
from warframe.worldstate.models import Arbitration, Cetus, OrbVallis

# define client
client = WorldstateClient()


# listed to any type of SingleQueryModel and TimedEvent
@client.listen_to(OrbVallis)  # decorate with the listen_to(type) function
async def on_arbi_state_change(
    vallis: OrbVallis,
) -> None:  # this function will be called if the state of the Type changes
    print("-" * 20)
    print(vallis)
    print("-" * 20)


async def main():
    print(
        (await client.query(OrbVallis))
    )  # this is just to have a reference to the current state
    on_arbi_state_change.start()  # start the listener
    await asyncio.sleep(3600)  # for testing, we wait an hour here
    on_arbi_state_change.stop()  # after an hour we stop the listener


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
