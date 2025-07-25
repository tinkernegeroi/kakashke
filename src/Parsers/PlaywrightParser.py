from playwright.async_api import async_playwright
from src.Parsers.Parser import Parser
import asyncio


class PlaywrightParser(Parser):
    def __init__(self, base_url):
        self.base_url = base_url
        self.browser = None
        self.context = None
        self.playwright = None
        self.page = None

    async def __aenter__(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=False)
        self.context = await self.browser.new_context()
        self.page = await self.context.new_page()
        await self.page.goto(self.base_url, timeout=10000)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"{exc_type=}, {exc_val=}, {exc_tb=}")
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()

    async def get_element_by_selector(self, selector):
        return await self.page.query_selector(selector)

    async def get_all_by_selector(self, selector):
        return await self.page.query_selector_all(selector)

    async def get_element_text_by_selector(self, selector):
        item = await self.get_element_by_selector(selector)
        return await item.inner_text()

    async def go_to_page(self, url):
        await self.page.goto(url, timeout=60000)

    async def wait_for_selector(self, selector):
        await self.page.wait_for_selector(selector)

    async def get_item_text(self, item, selector):
        el = await item.query_selector(selector)
        if not el:
            return None
        text = await el.inner_text()
        return text

    async def get_href(self, item, selector):
        el = await item.query_selector(selector)
        return await el.get_attribute("href") if el else None

    async def get_item_text_without_selector(self, item):
        return await item.inner_text()

    async def scroll_up(self):
        for i in range(6):
            await self.page.evaluate("window.scrollTo(0, -100000)")
            await asyncio.sleep(5)

    async def get_items_from_tg(self, target_url):
        await self.go_to_page(target_url)
        await self.scroll_up()
        await self.wait_for_selector(".tgme_container")
        items = await self.get_all_by_selector(".tgme_widget_message_wrap")
        return items
