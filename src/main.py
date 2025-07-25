import asyncio

from src.Handlers.AlfaHandler import AlfaHandler
from src.Handlers.CarcadeHandler import CarcadeHandler
from src.Handlers.GazpromHandler import GazpromHandler
from src.Services.CarcadeService import CarcadeService
from src.Services.GazpromService import GazpromService
from src.Handlers.VTBHandler import VTBHandler
from src.Services.VTBService import VTBService
from src.Parsers.PlaywrightParser import PlaywrightParser
from src.Services.AlfaService import AlfaService


async def main():
    vtb_base_url = "https://www.vtb-leasing.ru/auto-market/f/type-is-4/?PAGEN_1"
    gazprom_baze_url = "https://autogpbl.ru/avtomobili-i-tekhnika-s-probegom/?filter-type=4"
    alfa_url = "https://t.me/s/alfaleasing_probeg"
    carcade_url = "https://t.me/s/CarcadeStock"

    # async with PlaywrightParser(vtb_base_url) as parser:
    #     handler = VTBHandler()
    #     service = VTBService(parser, handler, vtb_base_url)
    #     data = await service.parse_all()
    #     for car in data:
    #         print(car)
    #
    # async with PlaywrightParser(gazprom_baze_url) as parser:
    #     handler = GazpromHandler()
    #     service = GazpromService(parser, handler, gazprom_baze_url)
    #     data = await service.parse_n_pages(gazprom_baze_url, 5)
    #     for car in data:
    #         print(car)
    #
    # async with PlaywrightParser(alfa_url) as parser:
    #     handler = AlfaHandler()
    #     tg_parser = AlfaService(parser, handler, alfa_url)
    #     await tg_parser.parse_page()

    async with PlaywrightParser(carcade_url) as parser:
        handler = CarcadeHandler()
        tg_parser = CarcadeService(parser, handler, carcade_url)
        await tg_parser.parse_page(carcade_url)



if __name__ == "__main__":
    asyncio.run(main())
