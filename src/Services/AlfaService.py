import asyncio

class AlfaService():
    def __init__(self, parser, handler, url):
        self.parser = parser
        self.handler = handler
        self.base_url = url

    async def parse_page(self):
        items = await self.parser.get_items_from_tg(self.base_url)
        for item in items:
            message_text = await self.parser.get_item_text(item, ".tgme_widget_message_text")
            text = self.handler.create_data_for_db(message_text)
            type = self.handler.get_type(text)
            if (type == "Грузовой автотранспорт") or (type == "Оборудование") or (type == "Спецтехника"):
                continue
            else:

                title = self.handler.get_title_from_text(text)
                price = self.handler.get_price_from_text(text)
                city = self.handler.get_city_from_text(text)
                year = self.handler.get_year_from_text(text)
                mileage = self.handler.get_mileage_from_text(text)
                result = {
                    "title": title,
                    "price": price,
                    "city": city,
                    "year": year,
                    "mileage": mileage,
                }
                print(result)