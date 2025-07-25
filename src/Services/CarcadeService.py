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
            title = self.handler.get_title_from_text(text)
            price = self.handler.get_price_from_text(text)
            result = {
                "title": title,
                "price": price
            }
            print(result)