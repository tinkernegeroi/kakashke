import asyncio

from GazpromHandler import GazpromHandler
from GazpromService import GazpromService
from VTBHandler import VTBHandler
from VTBService import VTBService
from PlaywrightParser import PlaywrightParser


async def main():
    vtb_base_url = "https://www.vtb-leasing.ru/auto-market/f/type-is-4/?PAGEN_1"
    gazprom_baze_url = "https://autogpbl.ru/avtomobili-i-tekhnika-s-probegom/?filter-type=4"
    # async with PlaywrightParser(vtb_base_url) as parser:
    #     handler = VTBHandler()
    #     service = VTBService(parser, handler, vtb_base_url)
    #     data = await service.parse_all()
    #     for car in data:
    #         print(car)

    async with PlaywrightParser(gazprom_baze_url) as parser:
        handler = GazpromHandler()
        service = GazpromService(parser, handler, gazprom_baze_url)
        data = await service.parse_page(gazprom_baze_url)
        for car in data:
            print(car)

if __name__ == "__main__":
    asyncio.run(main())
