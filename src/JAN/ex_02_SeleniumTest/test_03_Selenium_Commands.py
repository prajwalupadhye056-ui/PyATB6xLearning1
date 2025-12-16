import pytest
from selenium import webdriver
import allure


@allure.title("Verify Login page title of app.vwo.com")
def test_vmo_Sample():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title == "Login - VWO"

