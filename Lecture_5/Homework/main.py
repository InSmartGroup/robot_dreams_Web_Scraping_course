import json
import re
import requests
import sqlite3

url = r"https://www.lejobadequat.com/emplois"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://google.com"
}

payload = {
    "action": "facetwp_refresh",
    "data": {"facets": {"recherche": [], "ou": [], "type_de_contrat": [], "fonction": [], "load_more": [3]},
             "frozen_facets": {"ou": "hard"}, "http_params": {"get": [], "uri": "emplois", "url_vars": []},
             "template": "wp", "extras": {"counts": True, "sort": "default"}, "soft_refresh": 1, "is_bfcache": 1,
             "first_load": 0, "paged": 3}
}

response_post = requests.post(url, json=payload, headers=headers)

pattern = re.compile(r"(<h3 class=\\\"jobCard_title m-0\\\">([a-zA-Z0-9.\s/\\]+))")

data = re.findall(pattern, response_post.text)

jobs = [i[1] for i in data]

print(len(jobs))
