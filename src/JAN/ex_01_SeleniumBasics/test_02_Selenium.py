import time
from selenium import webdriver
import allure
import pytest


@allure.title("Open the app.vmo.com")
@pytest.mark.regression
def test_vmo_():
    driver = webdriver.Chrome()
    #1. This code is translated to API request
    #2. POST Request - browser DRIVER(Server)
    #3. Where it will create a Session or Fresh Copy Browser(chrome)
    #4. Session ID -16 digit will be created
    driver.get("https://app.vwo.com")
    print(driver.session_id)
    #5. GET -> GET API Request to navigate to particular page
    #6.browser will navigate to URL
    

    #Source code (Client) -> API Request W3C - Browser Driver(Server)- >Browser
