import asyncio
from VTBHandler import VTBHandler
from VTBService import VTBService
from PlaywrightParser import PlaywrightParser


async def main():
    base_url = "https://www.vtb-leasing.ru/auto-market/f/type-is-4/?PAGEN_1"
    async with PlaywrightParser(base_url) as parser:
        handler = VTBHandler()
        service = VTBService(parser, handler, base_url)
        data = await service.parse_all()
        for car in data:
            print(car)


if __name__ == "__main__":
    asyncio.run(main())
