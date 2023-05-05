import asyncio

from pyframe import WorldstateClient, Language


async def main():
    async with WorldstateClient() as client:
        cetus = await client.get_cetus(language=Language.English) # english is default
        print(cetus.__dict__)



if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())

    # These are all the attributes
    # VVVV 

    # {
    #     'expiry': datetime.datetime(2023, 5, 5, 9, 0), 
    #     'is_day': False, 
    #     'time_left': '21m 58s', 
    #     'activation': datetime.datetime(2023, 5, 5, 8, 10), 
    #     'start_string': None, 
    #     'active': None, 
    #     'state': 'night', 
    #     'short_string': '21m to Day'
    # }