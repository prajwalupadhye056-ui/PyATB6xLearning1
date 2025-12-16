
import pytest
from selenium import webdriver
import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from dotenv import load_dotenv
load_dotenv(".env1")
import os


@allure.title("VWO Login Negative Testcase")
@allure.description("TC1 - Negative TC - VWO Login with Invalid cred.")
@pytest.mark.negativevwologin
def test_app_vwo_login_chrome():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("URL"))

    #Link Text -Excact Match
   # anchor_tag_element=driver.find_element(By.LINK_TEXT,"Start a free trial")
    #anchor_tag_element.click()

   # assert driver.current_url=="https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

    #Partial Link Text-contains

    Partial_link_element=driver.find_element(By.PARTIAL_LINK_TEXT,"free trial")
    Partial_link_element.click()
    time.sleep(10)
    driver.quit()
