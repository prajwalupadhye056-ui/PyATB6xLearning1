from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Print the titles of the Ebay sites after searching")
@allure.description("Verify that 62 items are there for macmini")
def test_ebay():
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Step 1: Open eBay
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")

    # Step 2: Search for macmini
    search_box = driver.find_element(By.ID, "gh-ac")
    search_box.send_keys("macmini")

    element_button = driver.find_element(By.CSS_SELECTOR, ".gh-search-button__label")
    element_button.click()

    # Step 3: Get product titles (FIXED)
    list_of_items = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,
        "//span[@class='su-styled-text primary default']")))


    # Step 4: Get prices
    # Wait for prices
    list_of_item_prices = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//span[contains(@class,'s-card__price')]")
        )
    )

    print("\n===== Mac Mini Listings on eBay =====\n")

    print("Number of items found:", len(list_of_items))
    for i in list_of_items:
        print(i.text)

    print("Number of prices found:", len(list_of_item_prices))
    for j in list_of_item_prices:
        print(j.text)


    time.sleep(5)
    driver.quit()

