import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = r"https://www.lejobadequat.com/emplois"

    headers = {"User-Agent": "Mozilla/5.0",
               "Referer": "https://google.com"
               }

    page_number = 1

    for page in range(10):
        payload = {"action": "facetwp_refresh",
                   "data": {
                       "facets": {"recherche": [], "ou": [], "type_de_contrat": [], "fonction": [], "load_more": [2]},
                       "frozen_facets": {"ou": "hard"}, "http_params": {"get": [], "uri": "emplois", "url_vars": []},
                       "template": "wp", "extras": {"counts": True, "sort": "default"}, "soft_refresh": 1,
                       "is_bfcache": 1,
                       "first_load": 0, "paged": page_number}}

        response_post = requests.post(url, json=payload, headers=headers)

        soup = BeautifulSoup(response_post.content, "html.parser")

        a = soup.find_all("h3")

        jobs = []

        for i in a:
            i = str(i).split('<h3 class=\'\\"jobCard_title\' m-0\\"="">')
            i = str(i[1]).split('&lt;\\/h3&gt;')
            jobs.append(i[0])

        print(f"Page {page_number} - status code {response_post.status_code}")

        try:
            with open("job_titles.txt", "a") as file:
                for job in jobs:
                    file.write(job + "\n")

        except FileNotFoundError:
            with open("job_titles.txt", "w") as file:
                for job in jobs:
                    file.write(job + "\n")

        page_number += 1

    print("Scraping complete.")
