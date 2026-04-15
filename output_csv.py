import os
import csv

def save_to_csv(data):
    os.makedirs("output", exist_ok=True) # make new folder for the output csv

    with open("output/quotes.csv", "w", newline="", encoding="utf-8") as file: #create csv file
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author", "Tags"])
        writer.writerows(data)