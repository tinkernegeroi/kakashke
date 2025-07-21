class TgParser():
    def __init__(self, parser, handler):
        self.parser = parser
        self.handler = handler

    async def parse_page(self, target_url):
        await self.parser.go_to_page(target_url)
        await self.parser.scroll_up()
        await self.parser.wait_for_selector(".tgme_container")
        items = await self.parser.get_all_by_selector(".tgme_widget_message_wrap js-widget_message_wrap")
        print(items)
        for item in items:
            message_text = await self.parser.get_item_text(item, "body > main > div > section > div:nth-child(5) > div.tgme_widget_message.text_not_supported_wrap.js-widget_message > div.tgme_widget_message_bubble > div.tgme_widget_message_text.js-message_text.before_footer > div")
            print(message_text)