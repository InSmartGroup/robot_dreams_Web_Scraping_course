from bs4 import BeautifulSoup

import json
import re
import requests


# BeautifulSoup's find\find_all keyword attributes:
# tags (by default)
# class_="some class"
# id="some id"
# string="some string"
# it also supports regex (string=re.compile(r"regex pattern")


def parse_xml(xml_data, search_method="all", search_keyword=None, search_text=None):
    soup = BeautifulSoup(xml_data, features="xml")

    if search_method == "one":
        if search_text is not None:
            data = soup.find(string=search_text)
        elif search_keyword is not None:
            data = soup.find(search_keyword)

        return data

    elif search_method == "all":
        if search_keyword is not None:
            data = soup.find_all(search_keyword)
        elif search_text is not None:
            data = soup.find_all(string=search_text)

        return data

    else:
        print("In xml_keyword, type 'one' to find one element, or 'all' to find all elements.")


def parse_xml_regex(xml_data, key_tag, regex_pattern, search_mode="all"):
    soup = BeautifulSoup(xml_data, "xml")

    if search_mode == "all":
        return soup.find_all(key_tag, string=re.compile(regex_pattern))

    elif search_mode == "one":
        return soup.find(key_tag, string=re.compile(regex_pattern))

    else:
        print("In xml_keyword, type 'one' to find one element, or 'all' to find all elements.")


if __name__ == "__main__":

    xml_example = """<?xml version="1.0" encoding="UTF-8"?>
        <library>
            <book>
                <title>To Kill a Mockingbird</title>
                <author>Harper Lee</author>
                <year>1960</year>
                <isbn>978-0-06-112008-4</isbn>
            </book>
            <book>
                <title>1984</title>
                <author>George Orwell</author>
                <year>1949</year>
                <isbn>978-0-452-28423-4</isbn>
            </book>
            <book>
                <title>The Great Gatsby</title>
                <author>F. Scott Fitzgerald</author>
                <year>1925</year>
                <isbn>978-0-7432-7356-5</isbn>
            </book>
        </library>"""

    result = parse_xml(xml_example, search_keyword="author")
    print(result)

    result_regex = parse_xml_regex(xml_example, "title", r"[a-zA-Z0-9]+")
    print(result_regex)
