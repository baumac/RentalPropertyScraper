# This is a sample Python script.
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import csv
import random
import time


def get_listings(url_search_page):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe", options=options)
    driver.get(url_search_page)
    time.sleep(8)

    search_window = driver.current_window_handle

    with open("scrape_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Listing", "Gross Annual Income", "List Price", "Gross Annual Income / List Price"])

        listing_pages = driver.find_elements_by_xpath("//a[contains(@class, 'goToPage')]")

        for i in range(len(listing_pages)):
            listing_page = driver.find_elements_by_xpath("//a[contains(@class, 'goToPage')]")[i]

            if i == 0 or i == len(listing_pages) - 1:
                pass
            else:
                listing_page.click()

            listing_elements = listing_page.find_elements_by_xpath(
                "//*[@class='MapHomeCardReact HomeCard']")

            time.sleep(random.randint(5, 15))

            for z in range(len(listing_elements)):
                try:
                    listing = listing_page.find_elements_by_xpath(
                        "//*[@class='MapHomeCardReact HomeCard']")[z]

                    listing.click()
                    listing_window = [window for window in driver.window_handles if window != search_window][0]
                    driver.switch_to.window(listing_window)
                    result = process_listing(driver)
                    writer.writerow(result)
                    f.flush()
                    driver.close()
                    time.sleep(random.randint(3, 5))
                    driver.switch_to.window(search_window)
                except:
                    print("An exception occurred")

    return


def process_listing(driver):
    time.sleep(random.randint(5, 15))
    url_listing = driver.current_url
    gai_in_dollars = get_gross_annual_income(driver)
    lp_in_dollars = get_list_price(driver)

    if gai_in_dollars == -1 or lp_in_dollars == -1:
        ratio = -1
    else:
        ratio = gai_in_dollars/lp_in_dollars

    result = [url_listing, gai_in_dollars, lp_in_dollars, ratio]

    print(result)

    return result


def get_gross_annual_income(driver):

    try:
        element = driver.find_element_by_xpath(
            "//*[@class='entryItemContent' and contains(text(), 'Gross Annual Income:')]")
        gross_annual_income = int(element.text.split("$")[1].replace(',', ''))
        return gross_annual_income

    except NoSuchElementException:
        return -1


def get_list_price(driver):

    try:
        element = driver.find_element_by_xpath(
            "//*[@class='info-block price']").find_element_by_xpath("//*[@class='statsValue']")
        list_price = int(element.text.split("$")[1].replace(',', ''))
        return list_price

    except NoSuchElementException:
        return -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    get_listings("https://www.redfin.com/city/10943/MN/Minneapolis/filter/property-type=multifamily")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
