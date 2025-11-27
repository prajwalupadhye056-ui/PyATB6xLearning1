import time
from selenium import webdriver
import allure
import pytest


@allure.title("Open the app.vmo.com")
@pytest.mark.regression
def test_vmo_():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    time.sleep(10)
