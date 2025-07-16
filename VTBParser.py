from playwright.async_api import async_playwright


class VTBParser:
    def __init__(self, base_url):
        self.base_url = base_url
        self.browser = None
        self.context = None
        self.playwright = None
        self.page = None

    async def __aenter__(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=True)
        self.context = await self.browser.new_context()
        self.page = await self.context.new_page()
        await self.page.goto(self.base_url, timeout=60000)
        try:
            await self.page.click("a:has-text('Хорошо')")
        except:
            pass
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"{exc_type=}, {exc_val=}, {exc_tb=}")
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()

    async def parse_all(self):
        results = []
        await self.page.wait_for_selector(".t-page-navigation")
        pager = await self.page.query_selector_all(
            "#auto-list-cards-3 > div > div.t-market-section > div.t-page-navigation > div.t-pager-item.last > a"
        )
        last_page = [await p.inner_text() for p in pager][0]

        for page_n in range(1, last_page + 1):
            target_url = f"{self.base_url}={page_n}"
            await self.page.goto(target_url)
            page_results = await self.parse_page()
            results.extend(page_results)
        return results

    async def parse_page(self):
        await self.page.wait_for_selector(".t-market-section")
        items = await self.page.query_selector_all(".t-market-item")
        results = []

        for item in items:
            title_el = await item.query_selector(".t-market-auto-title")
            monthly_price_el = await item.query_selector(".t-market-auto-month-price")
            full_price_el = await item.query_selector(".t-market-auto-full-price")
            link_el = await item.query_selector("a.t-market-item-bottom-link")
            spec_el = await item.query_selector(".t-market-auto-props")

            title = (await title_el.inner_text()).strip() if title_el else None
            monthly_price = (await monthly_price_el.inner_text()).strip().replace("\xa0", "") if monthly_price_el else None
            full_price = (await full_price_el.inner_text()).strip().replace("\xa0", "") if full_price_el else None
            href = await link_el.get_attribute("href") if link_el else None
            url = f"https://www.vtb-leasing.ru{href}" if href and href.startswith("/") else href
            spec = (await spec_el.inner_text()).strip().replace("\xa0", "") if spec_el else None

            results.append({
                "title": title,
                "monthly_price": monthly_price,
                "full_price": full_price,
                "spec": spec,
                "url": url,
            })

        return results
