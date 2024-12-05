from bs4 import BeautifulSoup
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from Project.Parser.ws_headers import ws_headers

import json
import random
import re
import requests
import time


class Parser:
    def __init__(self, url, random_headers=False):
        self.url = url

        if random_headers:
            self.headers = random.choice(ws_headers)

        else:
            self.headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",
                "Referer": "https://www.google.com"
            }

        self.content = None
        self.domain_name = re.findall(r"((http|https)://[a-zA-Z0-9._-]+)", self.url)[0][0]

    def check_request_status(self):
        response = requests.get(self.url, headers=self.headers)
        print(response.status_code, response.reason)

    def parse(self, parser="lxml", sleep_timer=0, save_to_file=None):
        time.sleep(sleep_timer)

        response = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.content, features=parser)

        if save_to_file is not None:
            with open(f"{save_to_file}", "w", encoding="utf-8") as file:
                file.write(soup.prettify())

        self.content = soup

        return self.content

    def read_from_file(self, file_name: str):
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                content = file.read()

                self.content = BeautifulSoup(content, "lxml")

                return self.content

        except (FileExistsError, FileNotFoundError):
            return "File not found. Apply the 'get_data' method first."

    def search_html(self, tag: str, attrs: dict, find_all=False, sleep_timer=0):
        time.sleep(sleep_timer)

        if find_all:
            return self.content.find_all(tag, attrs)

        else:
            return self.content.find(tag, attrs)

    # def search_html_js(self):
    #     TODO: complete and test this function
    #     pass

    def search_xpath(self, xpath: str, sleep_timer=0):
        time.sleep(sleep_timer)

        tree = html.fromstring(str(self.content))

        return tree.xpath(xpath)

    # def search_xpath_js(self, url: str, search_by="xpath", wait_js=10):
    #     TODO: complete and test this function
    #     driver = webdriver.Chrome()
    #     wait = WebDriverWait(driver, timeout=wait_js)
    #
    #     search_methods = {
    #         "tag": By.TAG_NAME,
    #         "class": By.CLASS_NAME,
    #         "id": By.ID,
    #         "xpath": By.XPATH
    #     }
    #
    #     driver.get(url)

    @staticmethod
    def crawl(links: list, xpath_pattern: str, random_headers=False, sleep_timer=0):
        content = []

        for link in links:
            time.sleep(sleep_timer)
            parser = Parser(link, random_headers=random_headers)
            parser.parse()
            needed_item = parser.search_xpath(xpath_pattern)[0]
            content.append(needed_item)

        return content

    def change_headers(self):
        self.headers = random.choice(ws_headers)

    @staticmethod
    def to_json(filename: str, data: list):
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
