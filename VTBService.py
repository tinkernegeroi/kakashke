

class VTBService():
    def __init__(self, playwright_parser, vtb_handler, base_url):
        self.parser = playwright_parser
        self.handler = vtb_handler
        self.base_url = base_url

    async def parse_all(self):
        results = []
        await self.parser.wait_for_selector(".t-page-navigation")

        last_page = await self.parser.get_element_text_by_selector(
            "#auto-list-cards-3 > div > div.t-market-section > div.t-page-navigation > div.t-pager-item.last > a"
        )

        for page_n in range(1, int(last_page) + 1):
            target_url = f"{self.base_url}={page_n}"
            page_results = await self.parse_page(target_url)
            results.extend(page_results)
        return results

    async def parse_page(self, url):
        await self.parser.go_to_page(url)
        await self.parser.wait_for_selector(".t-market-section")
        items = await self.parser.get_all_by_selector(".t-market-item")
        results = []

        for item in items:
            title = await self.parser.get_item_text(item, ".t-market-auto-title")
            title = self.handler.delete_space(title) if title else title
            monthly_price = await self.parser.get_item_text(item, ".t-market-auto-month-price")
            monthly_price = self.handler.delete_space(monthly_price) if monthly_price else monthly_price
            full_price = await self.parser.get_item_text(item, ".t-market-auto-full-price")
            full_price = self.handler.delete_space(full_price) if full_price else full_price
            href = await self.parser.get_href(item, "a.t-market-item-bottom-link")
            url = self.handler.create_car_url(href)
            spec = await self.parser.get_item_text(item, ".t-market-auto-props")
            spec = self.handler.delete_space(spec) if spec else spec

            results.append({
                "title": title,
                "monthly_price": monthly_price,
                "full_price": full_price,
                "spec": spec,
                "url": url,
            })

        return results
