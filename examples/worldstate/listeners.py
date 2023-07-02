import asyncio
import logging

from warframe.worldstate import WorldstateClient, WorldstateLogger
from warframe.worldstate.models import Cetus, OrbVallis

# define logger
logger = WorldstateLogger("main_wsclient", logging.DEBUG)
logger.addHandler(logging.StreamHandler())

# define client
client = WorldstateClient(logger=logger)


# listed to any type of SingleQueryModel and TimedEvent
@client.listen_to(OrbVallis)  # decorate with the listen_to(type) function
# this function will be called if the state of the Type changes
async def on_vallis_state_change(
    vallis: OrbVallis,  # this function will be called if the state of the Type changes
) -> None:
    print("-" * 20)
    print("ORB VALLIS")
    print(vallis)
    print("-" * 20)


@client.listen_to(Cetus)
async def on_cetus_state_change(cetus: Cetus):
    print("-" * 20)
    print("CETUS")
    print(cetus)
    print("-" * 20)


async def main():
    print(
        (await client.query(OrbVallis))
    )  # this is just to have a reference to the current state
    print(
        (await client.query(Cetus))
    )  # this is just to have a reference to the current state
    on_vallis_state_change.start()  # start the listener
    on_cetus_state_change.start()
    await asyncio.sleep(3600)  # for testing, we wait an hour here
    on_vallis_state_change.stop()  # after an hour we stop the listener
    on_cetus_state_change.stop()
    await client.close()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
