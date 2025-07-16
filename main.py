import asyncio
from playwright.async_api import async_playwright

TARGET_URL = (
    "https://www.vtb-leasing.ru/auto-market/"
    "f/"
    "type-is-4/?PAGEN_1"
)

async def parse_all(page, base_url):
    results = []
    await page.wait_for_selector(".t-page-navigation")
    pager = await page.query_selector_all("#auto-list-cards-3 > div > div.t-market-section > div.t-page-navigation > div.t-pager-item.last > a")
    last_page = [await p.inner_text() for p in pager][0]
    for page_n in range(1, int(last_page) + 1):
        target_url = base_url + "=" + str(page_n)
        await page.goto(target_url)
        result = await parse_page(page)
        results.append(result)
    return results


async def parse_page(page):
    await page.wait_for_selector(".t-market-section")
    items = await page.query_selector_all(".t-market-item")
    results = []
    for item in items:
        title_nf = await item.query_selector(".t-market-auto-title")
        monthly_price_nf = await item.query_selector(".t-market-auto-month-price")
        full_price_nf = await item.query_selector(".t-market-auto-full-price")
        link_el = await item.query_selector("a.t-market-item-bottom-link")
        all_specification = await item.query_selector(".t-market-auto-props")

        title = (await title_nf.inner_text()).strip()
        monthly_price = (await monthly_price_nf.inner_text()).strip().replace("\xa0", "") if monthly_price_nf else None
        full_price = (await full_price_nf.inner_text()).strip().replace("\xa0", "") if full_price_nf else None
        href = await link_el.get_attribute("href") if link_el else None
        url = "https://www.vtb-leasing.ru" + href if href and href.startswith("/") else href
        spec = (await all_specification.inner_text()).strip().replace("\xa0", "") if all_specification else None
        # hp = spec[0] if len(spec) == 1 else None
        # city = spec[0] if len(spec) > 1 else None
        # mileage = spec[1] if len(spec) > 1 else None
        # year = spec[2] if len(spec) > 1 else None

        results.append({
            "title": title,
            "monthly_price": monthly_price,
            "full_price": full_price,
            "spec": spec,
            "url": url,
        })

    return results

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(TARGET_URL, timeout=60000)
        try:
            await page.click("a:has-text('Хорошо')")
        except:
            pass
        data = await parse_all(page, TARGET_URL)

        for slov in data:
            for car in slov:
                print(car)
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
