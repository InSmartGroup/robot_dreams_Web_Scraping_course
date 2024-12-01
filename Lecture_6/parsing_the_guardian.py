import json
import requests

from bs4 import BeautifulSoup


def initial_parse(url):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.google.com"
    }

    response = requests.get(url, headers=headers)

    print(response.text)

    if response.status_code == 200:

        with open("html_result.html", "w", encoding="utf-8") as file:
            file.write(response.text)

    else:
        print(response.status_code, response.reason)


def parse_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    soup = BeautifulSoup(content, "html.parser")

    return soup


def parse_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.google.com"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    return soup


if __name__ == "__main__":
    # initial_parse(r"https://www.theguardian.com/uk/travel/")

    # soup_file = parse_file("./html_result.html")

    soup = parse_url(r"https://www.theguardian.com/uk/travel/")

    travel = soup.find("section", attrs={"id": "travel"})

    div = travel.find_all("div", attrs={"class": "dcr-f9aim1"})

    data = []

    for i in div:
        url = i.find("a").get("href")
        url = f"https://www.theguardian.com/uk{url}"
        region = i.find("h3", {"class": "card-headline"}).search_html("div").text
        title = i.find("h3", {"class": "card-headline"}).search_html("span").text

        data.append({
            "url": url,
            "region": region,
            "title": title
        })

    with open("parsing_the_guardian_result.json", "w") as file:
        json.dump(data, file, indent=4)
