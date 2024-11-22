import scrapy  # pip install Scrapy

url = r"https://www.coinmarketcap.com"

# to create a new scrapy project, in terminal:
# 1. scrapy startproject <project name>
# 2. scrapy genspider <spider name> <website URL>
# 3. scrapy crawl <spider name>
# to write scraped data to file, in terminal:
# scrapy crawl <spider name> -o file.json (or file.csv)

"""
import scrapy


class HomeworkSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    custom_settings = {
        "DOWNLOAD_DELAY": 2
    }

    def parse(self, response, **kwargs):
        quotes = response.xpath("//div[contains@(class, 'quote')]").getall()

        for quote in quotes:
            text = quote.xpath(".//span[@class, 'text']/text()").get()
            author = quote.xpath(".//small[@class, 'author']/text()").get()

            yield {
                "quote": quote,
                "author": author
            }
"""