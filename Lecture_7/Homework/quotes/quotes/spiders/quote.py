import scrapy
import sqlite3


class HomeworkSpider(scrapy.Spider):
    name = "quote"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    custom_settings = {
        "DOWNLOAD_DELAY": 1
    }

    # define scraping threshold
    start_with_page = 1
    end_with_page = 2

    def parse(self, response, **kwargs):
        quotes = response.xpath("//div[contains(@class, 'quote')]")

        # create SQL database
        sql_filename = "quotes.db"
        connection = sqlite3.connect(sql_filename)
        cursor = connection.cursor()

        sql = """
            CREATE TABLE IF NOT EXISTS quotes (
            ID INTEGER PRIMARY KEY,
            quote TEXT NOT NULL,
            author TEXT NOT NULL,
            UNIQUE (quote, author)
            )
        """

        cursor.execute(sql)

        # find the needed data
        for quote in quotes:
            text = quote.xpath(".//span[@class='text']/text()").get().replace("“", "").replace("”", "")
            author = quote.xpath(".//small[@class='author']/text()").get()

            yield {
                "quote": text,
                "author": author,
            }

            # add data to the database
            sql = """
                INSERT INTO quotes (text, author),
                VALUES(?, ?)
                
            """
            cursor.execute(sql, __parameters=(text, author))

        # define the next page button
        next_page = response.xpath("//ul[@class='pager']//a/@href").get()
        next_page = f"https://quotes.toscrape.com{next_page}"

        if next_page is not None and self.start_with_page < self.end_with_page:
            self.start_with_page += 1
            yield response.follow(next_page, callback=self.parse)
