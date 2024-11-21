from bs4 import BeautifulSoup

import json
import requests

url = r"https://www.bbc.com/sport"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Referer": "https://www.google.com"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

# identify all the articles in the website's HTML
articles_list = soup.find("ul", {"class": "ssrcss-1xxqo5f-Grid e12imr580"})

data = []  # to store parsed data

# process each of the articles
articles = articles_list.find_all("div", {"type": "article"})

for i in articles[:5]:  # we need only the first 5 articles
    # find the link in the article
    link_raw = i.find("a", {"class": "ssrcss-zmz0hi-PromoLink exn3ah91"}).get("href")
    link = "https://www.bbc.com" + str(link_raw)

    # get HTML content from each of found links
    response = requests.get(link, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # parse topics inside those HTML pages
    topics = soup.find_all("a", {"class": "ssrcss-1ef12hb-StyledLink ed0g1kj0"})
    topics_list = [i.get_text() for i in topics]

    # add the needed data to the list
    data.append({
        "link": link,
        "topics": topics_list
    })

# write data to JSON
with open("result.json", "w") as file:
    json.dump(data, file, indent=4)
