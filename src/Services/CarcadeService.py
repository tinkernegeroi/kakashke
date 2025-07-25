class CarcadeService:
    def __init__(self, playwright_parser, handler, base_url):
        self.parser = playwright_parser
        self.handler = handler
        self.base_url = base_url

    async def parse_page(self, url):
        items = await self.parser.get_items_from_tg(url)
        for item in items:
            message_text = await self.parser.get_item_text(item, ".tgme_widget_message_text")
            print(message_text)