from session import session
from scrape_qoutes import scrape_quotes
from output_csv import save_to_csv

def main():
    driver = session()

    try:
        data = scrape_quotes(driver)
        save_to_csv(data)
        print("Done. Saved to output/quotes.csv")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()