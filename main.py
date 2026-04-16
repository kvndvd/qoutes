import os
import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

BASE_URL = "https://quotes.toscrape.com/"

def session():
    # options = Options()
    # options.add_argument("--headless")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome()
    return driver

def scrape_quotes():
    print("Starting main.py")
    driver = session()
    quotes_data = []
    seen = set()

    driver.get(BASE_URL)
    print(f"Opening link {BASE_URL}")

    while True:
        time.sleep(1)


        quotes = driver.find_elements(By.CSS_SELECTOR, "div.quote")
        print("Gathering data...")

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
            next_button.click()
        except NoSuchElementException:
            break

    driver.quit()
    return quotes_data

def save_to_csv(data):
    os.makedirs("output", exist_ok=True) # make new folder for the output csv

    with open("output/quotes.csv", "w", newline="", encoding="utf-8") as file: #create csv file
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