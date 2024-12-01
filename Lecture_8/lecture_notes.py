from Project.Parser.parser import Parser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

import json

# URL = r"https://www.tmforum.org/membership/current-members/"

URL = r"https://jobs.aon.com/jobs"


def parse():
    driver = webdriver.Chrome()

    max_page = 3

    wait = WebDriverWait(driver, timeout=10)

    result = []

    for page in range(1, max_page):
        driver.get(f"{URL}?page={page}")

        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "job-title-link")))

        jobs = driver.find_elements(By.CLASS_NAME, "job-title-link")

        for job in jobs:
            url = job.get_attribute("href")
            title = job.find_element(By.TAG_NAME, "span").text

            result.append({
                "url": url,
                "title": title
            })

    driver.quit()

    with open("result.json", "w") as file:
        json.dump(result, file, indent=4)


parse()
