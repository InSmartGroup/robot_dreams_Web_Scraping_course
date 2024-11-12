from bs4 import BeautifulSoup

import pandas as pd
import json
import re
import requests
import sqlite3

url = r"https://www.lejobadequat.com/emplois"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://google.com"
}

page_index = 2

if __name__ == "__main__":
    payload = {
        "action": "facetwp_refresh",
        "data": {"facets": {"recherche": [], "ou": [], "type_de_contrat": [], "fonction": [], "load_more": [3]},
                 "frozen_facets": {"ou": "hard"}, "http_params": {"get": [], "uri": "emplois", "url_vars": []},
                 "template": "wp", "extras": {"counts": True, "sort": "default"}, "soft_refresh": 1, "is_bfcache": 1,
                 "first_load": 0, "paged": page_index}
    }

    response_post = requests.post(url, json=payload, headers=headers)

    pattern_jobs = re.compile(r"(<h3 class=\\\"jobCard_title m-0\\\">([a-zA-Z0-9.\s/\\]+))")
    # pattern_links = re.compile(r"(<a href=\\\"(https.*?)\s?(title=\\\".*?\\\")\s?(class=\\\"jobCard_link\\\"))")

    soup = BeautifulSoup(response_post.content, "html.parser")

    data_jobs = re.findall(pattern_jobs, response_post.text)

    jobs = [i[1].strip() for i in data_jobs]
    links = [i["href"] for i in soup.find_all("a", title=True, href=True)]

    df = pd.DataFrame(columns=["jobTitle", "jobLink"])
    df["jobTitle"] = jobs
    df["jobLink"] = links
