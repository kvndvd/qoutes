import time
from session import session
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


BASE_URL = "https://quotes.toscrape.com/"

def scrape_quotes(driver):
    driver = session()
    quotes_data = []
    seen = set()

    driver.get(BASE_URL)

    while True:
        time.sleep(1)

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
            next_button.click()
        except NoSuchElementException:
            break

    return quotes_data