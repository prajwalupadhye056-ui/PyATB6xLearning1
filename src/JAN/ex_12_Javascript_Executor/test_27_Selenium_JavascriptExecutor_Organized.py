import allure
import time

from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.devtools.v140.input_ import MouseButton
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from allure_commons.types import AttachmentType

from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


class TestSelenium:

    def __init__(self):
        self.driver = None

    def openBrowser(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://selectorshub.com/xpath-practice-page/")
        self.driver.maximize_window()

    def test_verify_JS(self):
        title = self.driver.execute_script("return document.title;")
        print("Title:", title)

        url = self.driver.execute_script("return document.URL;")
        print("URL:", url)

    def close_browser(self):
        time.sleep(5)
        self.driver.quit()


test =TestSelenium()
test.openBrowser()
test.test_verify_JS()
test.close_browser()













