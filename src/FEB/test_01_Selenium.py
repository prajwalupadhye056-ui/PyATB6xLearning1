import pytest
from selenium import webdriver
import allure


@allure.title("Verify Login page title of EspoCRM Demo")

def test_vmo_Sample():
    driver = webdriver.Chrome()
    driver.get("https://demo.us.espocrm.com/")

    print(driver.title)
    assert driver.title == "EspoCRM Demo"

    print(driver.current_url)
    assert driver.current_url == "https://demo.us.espocrm.com/"
