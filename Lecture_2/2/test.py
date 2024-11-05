import requests
from bs4 import BeautifulSoup

url = r"https://46.itknyga.com.ua/grade/report/user/index.php?id=8"

response = requests.get(url=url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
print(f"Status code: {response.status_code}")

soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

print(soup.find_all("a href"))
