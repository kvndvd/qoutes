from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def session():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    return driver