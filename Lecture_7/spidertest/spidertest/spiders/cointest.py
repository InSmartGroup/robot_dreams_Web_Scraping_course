import scrapy


class CoinTestSpider(scrapy.Spider):
    name = "cointest"
    allowed_domains = ["https://coinmarketcap.com"]
    start_urls = ["https://coinmarketcap.com"]

    # define how many pages we'd want to scrap
    start = 0
    end = 2

    # define setting that are specific for this particular crawler
    # also, don't forget to add the user-agent information to the settings.py file
    custom_settings = {
        "DOWNLOAD_DELAY": 1
    }

    # describes the overall scraping logic
    def parse(self, response, **kwargs):
        rows = response.xpath("//table[contains(@class, 'cmc-table')]/tbody/tr")

        for row in rows:
            coin_name = row.xpath(
                ".//p[contains(@class, 'coin-item-symbol')]/text()|.//span[contains(@class, 'crypto-symbol')]/text()"
            ).get()

            coin_price = row.xpath(
                ".//td[4]//span/text()|.//td[4]/text()"
            ).getall()  # ["$", "0.001"]
            coin_price = "".join(coin_price)  # "$0.001"

            yield {
                "coin name": coin_name,
                "coin price": coin_price
            }

        # define the logic for going to the next web page
        next_page = response.xpath("//li[contains(@class, 'next')]/a/@href").get()
        next_page = f"https://coinmarketcap.com{next_page}"

        # stop scraping logic
        if next_page is not None and self.start < self.end:
            self.start += 1

            # if we're not stopping the process, define the logic for going to the next web page
            yield response.follow(next_page, callback=self.parse)
