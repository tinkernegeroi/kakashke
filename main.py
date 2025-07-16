import asyncio
from VTBParser import VTBParser


async def main():
    async with VTBParser("https://www.vtb-leasing.ru/auto-market/f/type-is-4/?PAGEN_1") as parser:
        data = await parser.parse_all()
        for car in data:
            print(car)


if __name__ == "__main__":
    asyncio.run(main())
