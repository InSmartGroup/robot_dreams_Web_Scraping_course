from bs4 import BeautifulSoup

import csv
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


def write_sql(data: list):
    filename = "../Outputs/result.db"

    connection = sqlite3.connect(filename)
    cursor = connection.cursor()

    sql_request = """
        CREATE TABLE IF NOT EXISTS jobs (
        ID INTEGER PRIMARY KEY,
        job_title TEXT NOT NULL,
        job_url TEXT NOT NULL,
        UNIQUE (job_title, job_url)
        )
    """

    cursor.execute(sql_request)

    for i in data:
        cursor.execute("""
            INSERT INTO jobs (job_title, job_url)
            VALUES (?, ?)
        """, (i["job_title"], i["job_url"]))

    connection.commit()

    connection.close()


def read_sql():
    filename = "../Outputs/result.db"

    connection = sqlite3.connect(filename)
    cursor = connection.cursor()

    sql = """
        SELECT job_title, job_url
        FROM jobs
    """

    response = cursor.execute(sql).fetchall()
    print(response)


if __name__ == "__main__":
    payload = {
        "action": "facetwp_refresh",
        "data": {"facets": {"recherche": [], "ou": [], "type_de_contrat": [], "fonction": [], "load_more": [3]},
                 "frozen_facets": {"ou": "hard"}, "http_params": {"get": [], "uri": "emplois", "url_vars": []},
                 "template": "wp", "extras": {"counts": True, "sort": "default"}, "soft_refresh": 1, "is_bfcache": 1,
                 "first_load": 0, "paged": page_index}
    }

    response_post = requests.post(url, json=payload, headers=headers)

    soup = BeautifulSoup(response_post.content, "html.parser")

    # define regex patterns
    pattern_jobs = re.compile(r"(<h3 class=\\\"jobCard_title m-0\\\">([a-zA-Z0-9.\s/\\]+))")

    # parse jobs data
    data_jobs = re.findall(pattern_jobs, response_post.text)

    # separate job names from job urls
    jobs = [i[1].strip() for i in data_jobs]
    links = [i["href"] for i in soup.find_all("a", title=True, href=True)]

    # structure data
    data_structured = [
        {
            "job_title": j[0],
            "job_url": j[1]
        }
        for j in zip(jobs, links)
    ]

    # write structured data to json
    with open("../Outputs/result.json", "w") as file:
        json.dump(data_structured, file, indent=4)

    # create a DB
    write_sql(data_structured)

    # read DB
    read_sql()

    # save data as CSV
    with open("../Outputs/result.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["job_title", "job_url"])
        writer.writerows(zip(jobs, links))
