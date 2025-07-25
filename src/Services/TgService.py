import asyncio

class TgService():
    def __init__(self, parser, handler):
        self.parser = parser
        self.handler = handler

    async def parse_page(self, target_url):
        await self.parser.go_to_page(target_url)
        await self.parser.scroll_up()
        await self.parser.wait_for_selector(".tgme_container")
        items = await self.parser.get_all_by_selector(".tgme_widget_message_wrap")
        for item in items:
            message_text = await self.parser.get_item_text(item, ".tgme_widget_message_text")
            text = self.handler.create_data_for_db(message_text)
            print(text)