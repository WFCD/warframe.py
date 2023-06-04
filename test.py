# queries are just another way to get the data to the corresponding objects.
# this is really just personal preference.

import asyncio

from pyframe.worldstate import WorldstateClient, Faction
from pyframe.worldstate.models import VoidTrader

json = """
{"id":"5d1e07a0a38e4a4fdd7cefca","activation":"2023-06-02T13:00:00.000Z","startString":"-1d 21h 4m 45s","expiry":"2023-06-04T13:00:00.000Z","active":true,"character":"Baro Ki'Teer","location":"Kronia Relay (Saturn)","inventory":[{"item":"Thrax Sigil","ducats":50,"credits":55000},{"item":"Primed Fever Strike","ducats":350,"credits":200000},{"item":"High Voltage","ducats":300,"credits":150000},{"item":"Prisma Tetra","ducats":400,"credits":50000},{"item":"Stalker Beacon","ducats":200,"credits":125000},{"item":"Baro Ki'teer Glyph","ducats":80,"credits":50000},{"item":"Weapon Glaive On Kill Buff Secondary","ducats":300,"credits":115000},{"item":"Ki'teer Kubrow Armor","ducats":500,"credits":250000},{"item":"Xiphos Prisma Skin","ducats":220,"credits":400000},{"item":"Ki'teer Razza Synadana","ducats":400,"credits":350000},{"item":"Quanta Aufeis Skin","ducats":300,"credits":300000},{"item":"Ki'teer Atmos Diadem","ducats":525,"credits":375000},{"item":"Prisma Grinlok","ducats":500,"credits":220000},{"item":"Pack Leader Emblem","ducats":50,"credits":50000},{"item":"Sima Luxxum Ornament","ducats":100,"credits":100000},{"item":"Paracesis Elixis Skin","ducats":350,"credits":350000},{"item":"Liset Prop Grineer Cutter","ducats":100,"credits":100000},{"item":"Prisma Dual Decurions","ducats":525,"credits":175000},{"item":"Deimos Veolicpod Prex","ducats":75,"credits":100000},{"item":"Mulciber Shoulder Plate","ducats":315,"credits":215000},{"item":"Mulciber Leg Plate","ducats":300,"credits":200000},{"item":"Mulciber Chest Plate","ducats":325,"credits":250000},{"item":"Ivara Leverian Povis Records Decoration","ducats":75,"credits":100000},{"item":"Fae Path Ephemera","ducats":15,"credits":1000},{"item":"Sands Of Inaros Blueprint","ducats":100,"credits":25000}],"psId":"5d1e07a0a38e4a4fdd7cefca25","endString":"2h 55m 14s","initialStart":"1970-01-01T00:00:00.000Z","schedule":[]}
"""


async def main():
    async with WorldstateClient() as client:
        # import from models and pass the type you want the object of
        void_trader = VoidTrader._from_json(json)
        for item in void_trader.inventory:
            print(item)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
