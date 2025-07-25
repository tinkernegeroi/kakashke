import asyncio

class AlfaService():
    def __init__(self, parser, handler):
        self.parser = parser
        self.handler = handler

    async def parse_page(self, target_url):
        items = await self.parser.get_items_from_tg(target_url)
        for item in items:
            message_text = await self.parser.get_item_text(item, ".tgme_widget_message_text")
            type = self.handler.get_type(message_text)
            if (type == "Грузовой автотранспорт") or (type == "Оборудование") or (type == "Спецтехника"):
                continue
            else:
                title = self.handler.get_title_from_text(message_text)
                city = self.handler.get_city_from_text(message_text)
                year = self.handler.get_year_from_text(message_text)
                mileage = self.handler.get_mileage_from_text(message_text)
                result = {
                    "title": title,
                    "city": city,
                    "year": year,
                    "mileage": mileage,
                }
                print(result)