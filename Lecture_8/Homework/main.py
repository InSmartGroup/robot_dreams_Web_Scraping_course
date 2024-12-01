from bs4 import BeautifulSoup
from selenium import webdriver

import json
import lxml
import random
import requests


def get_user_agents():
    url = r"https://hasdata.com/blog/user-agents-for-web-scraping"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Referer": "https://www.google.com"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "lxml")

    table = soup.find("div", attrs={"class": "rounded-2xl border overflow-x-auto"})
    rows = table.find_all("td")

    user_agents = []

    for row in rows[1::2]:
        user_agents.append({
            "User-Agent": row.text
        })

    with open("user_agents.json", "w") as file:
        json.dump(user_agents, file, indent=4)

    return user_agents


if __name__ == "__main__":
    user_agents = get_user_agents()

    print(user_agents[5]["User-Agent"])
