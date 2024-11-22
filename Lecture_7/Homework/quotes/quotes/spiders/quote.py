import scrapy


class HomeworkSpider(scrapy.Spider):
    name = "quote"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    custom_settings = {
        "DOWNLOAD_DELAY": 1
    }

    starting_with_page = 1
    end_with_page = 2

    def parse(self, response, **kwargs):
        quotes = response.xpath("//div[contains(@class, 'quote')]")

        for quote in quotes:
            text = quote.xpath(".//span[@class='text']/text()").get().replace("“", "").replace("”", "")
            author = quote.xpath(".//small[@class='author']/text()").get()

            yield {
                "quote": text,
                "author": author,
            }

        next_page = response.xpath("//ul[@class='pager']//a/@href").get()
        next_page = f"https://quotes.toscrape.com{next_page}"

        if next_page is not None and self.starting_with_page < self.end_with_page:
            self.starting_with_page += 1
            yield response.follow(next_page, callback=self.parse)
