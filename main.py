import asyncio
from Handlers.GazpromHandler import GazpromHandler
from Services.GazpromService import GazpromService
from Handlers.VTBHandler import VTBHandler
from Services.VTBService import VTBService
from Parsers.PlaywrightParser import PlaywrightParser
from Services.TgService import TgService


async def main():
    vtb_base_url = "https://www.vtb-leasing.ru/auto-market/f/type-is-4/?PAGEN_1"
    gazprom_baze_url = "https://autogpbl.ru/avtomobili-i-tekhnika-s-probegom/?filter-type=4"
    alfa_url = "https://t.me/s/alfaleasing_probeg"

    async with PlaywrightParser(vtb_base_url) as parser:
        handler = VTBHandler()
        service = VTBService(parser, handler, vtb_base_url)
        data = await service.parse_all()
        for car in data:
            print(car)

    async with PlaywrightParser(gazprom_baze_url) as parser:
        handler = GazpromHandler()
        service = GazpromService(parser, handler, gazprom_baze_url)
        data = await service.parse_n_pages(gazprom_baze_url, 5)
        for car in data:
            print(car)

    async with PlaywrightParser(alfa_url) as parser:
        handler = VTBHandler()
        tg_parser = TgService(parser, handler)
        await tg_parser.parse_page(alfa_url)


if __name__ == "__main__":
    asyncio.run(main())
