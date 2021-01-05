# This is a Python script to scrape a Rental Property listings for useful data.
#
# In it's current state this project scrapes a Redfin property listing search
# to find the listings with the best price to rental income ratio.
#
# The results are then stored in a csv file, and emailed to the desired recipient.

import yaml

from RentalPropertyScraper.Redfin.scrapeSite import scrape_redfin_search

from RentalPropertyScraper.Utils.sendEmail import send_email_with_attachment

if __name__ == '__main__':

    print("Running main.py")

    with open("config.yaml", "r") as ymlfile:
        cfg = yaml.full_load(ymlfile)

    RedfinResultsFilePath = scrape_redfin_search(cfg)

    print("Created Redfin results file: " + RedfinResultsFilePath)

    response = send_email_with_attachment(RedfinResultsFilePath, cfg)

    if response == 0:
        print("Emailed scraping result file(s) to: " + cfg["email"]["toEmail"]["address"])
    else:
        print("Failed to emailed scraping result file(s) to: " + cfg["email"]["toEmail"]["address"])

