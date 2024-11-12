from bs4 import BeautifulSoup
import requests
import re



jobs_per_page = 10

url = fr"https://jooble.org/SearchResult?p=4&rgns=Virginia&ukw=artificial%20intelligence"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
           "Referer": "https://jooble.org/SearchResult?p=3&rgns=Virginia&ukw=artificial%20intelligence"}

payload = {"search": "artificial intelligence", "region": "Virginia", "regionId": 47, "isCityRegion": "false",
           "jobTypes": [], "coords": "null", "page": 4, "isRemoteItSerp": "false", "workTitle": "null"}

response_get = requests.get(url, headers=headers)
response_post = requests.post(url, json=payload, headers=headers)

print(response_post.status_code, response_post.reason)
