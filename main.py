import os
import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

BASE_URL = "https://quotes.toscrape.com/"

def session():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(30)
    return driver

def scrape_quotes():
    print("Starting main.py")
    driver = session()
    quotes_data = []
    seen = set()

    try:
        driver.get(BASE_URL)
        print(f"Opening link {BASE_URL}")
        print("Gathering data...")
        while True:
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.quote"))
            )
            quotes = driver.find_elements(By.CSS_SELECTOR, "div.quote")
            for quote in quotes:
                text = quote.find_element(By.CSS_SELECTOR, "span.text").text
                author = quote.find_element(By.CSS_SELECTOR, "small.author").text
                tags = quote.find_elements(By.CSS_SELECTOR, "a.tag")
                tag_list = [tag.text for tag in tags]

                key = (text, author)
                if key not in seen:
                    seen.add(key)
                    quotes_data.append([text, author, ", ".join(tag_list)])
            try:
                next_button = driver.find_element(By.CSS_SELECTOR, "li.next a")
                ActionChains(driver).move_to_element(next_button).click(next_button).perform()
                time.sleep(1)
            except NoSuchElementException:
                break
        return quotes_data
    finally:
        driver.quit()

def save_to_csv(data):
    os.makedirs("output", exist_ok=True)

    with open("output/quotes.csv", "w", newline="", encoding="utf-8") as file:
        print("Saving to csv file")
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author", "Tags"])
        writer.writerows(data)

def main():
    data = scrape_quotes()
    save_to_csv(data)
    print("Done. Saved to output/quotes.csv")

if __name__ == "__main__":
    main()