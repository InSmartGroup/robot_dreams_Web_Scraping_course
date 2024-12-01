import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, timeout=10)

max_page = 3

result = []

for page in range(1, max_page):
    driver.get(f"https://jobs.marksandspencer.com/job-search?country%5B0%5D=United%20Kingdom&page={page}&radius=")

    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "ais-Hits-item")))

    elements = driver.find_elements(By.CLASS_NAME, "ais-Hits-item")

    for element in elements:
        title = element.find_element(By.TAG_NAME, "h3").text
        url = element.find_element(By.XPATH, ".//a[@class='c-btn c-btn--primary | [ mt-16 | md.mt-0 ]']").get_property("href")

        result.append({
            "title": title,
            "url": url
        })
#
with open("result.json", "w") as file:
    json.dump(result, file, indent=4)
