import pytest
from selenium import webdriver
import allure


@allure.title("Verify Login page title of app.vwo.com")
def test_vmo_Sample():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    if "PURA Healthcare Service" in driver.page_source:
        print("Text found! Test Case Passed!")
    else:
        print("Text not found!!!!")
        pytest.fail("Text not found on the page")


