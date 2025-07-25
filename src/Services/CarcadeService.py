class CarcadeService:
    def __init__(self, playwright_parser, handler, base_url):
        self.parser = playwright_parser
        self.handler = handler
        self.base_url = base_url

    async def parse_page(self, url):
        items = await self.parser.get_items_from_tg(url)
        for item in items:
            message_text = await self.parser.get_item_text(item, ".tgme_widget_message_text")
            text = self.handler.create_data_for_db(message_text)
            hashtags = self.handler.get_hashtags_from_text(text)
            if "#Легковые_CARCADE" in hashtags:
                title = self.handler.get_title_from_text(text)
                price = self.handler.get_price_from_text(text)
                year = self.handler.get_year_from_text(text)
                city = self.handler.get_city_from_text(text)
                mileage = self.handler.get_mileage_from_text(text)
                result = {
                    "title": title,
                    "price": price,
                    "year": year,
                    "city": city,
                    "mileage": mileage
                }
                print(result)
            else:
                continue