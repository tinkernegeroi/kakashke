
class GazpromService():
    def __init__(self, playwright_parser, handler, base_url):
        self.parser = playwright_parser
        self.handler = handler
        self.base_url = base_url

    async def parse_page(self, url):
        await self.parser.go_to_page(url)
        await self.parser.wait_for_selector(".izt-list-content-container")
        items = await self.parser.get_all_by_selector(".equipment-card-wrapper")
        results = []

        for item in items:
            title = await self.parser.get_item_text(item, ".catalog-car-card__wide-title")
            title = self.handler.delete_space(title) if title else None
            full_price = await self.parser.get_item_text(item, ".catalog-car-card__third-col-wide-price")
            full_price = self.handler.delete_space(full_price) if full_price else None
            monthly_price = await self.parser.get_item_text(item, ".catalog-car-card__payment-info")
            monthly_price = self.handler.delete_space(monthly_price) if monthly_price else None
            specs = await self.parser.get_item_text(item, ".catalog-car-card__add-info ")

            href = await self.parser.get_href(item, "a.catalog-car-card__wide-title")
            url = self.handler.create_url(href)
            results.append({
                "title": title,
                "full_price": full_price,
                "monthly_price": monthly_price,
                "specs": specs,
                "url": url
            })

        return results

    async def parse_n_pages(self, url, n):
        data = []
        for page_n in range(1, n+1):
            target_url = url + "&page=" + str(page_n)
            result = await self.parse_page(target_url)
            data.extend(result)
        return data