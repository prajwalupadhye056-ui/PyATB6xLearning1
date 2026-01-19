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


@allure.title("SVG")
@allure.description("Verify SVG")
def test_verify_SVG():


    driver = webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")


    list_of_states= driver.find_elements(By.XPATH,"//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")


    for state in list_of_states:
        print(state.get_attribute("aria-label"))

        if "Tripura" in state.get_attribute("aria-label"):
            state.click()
            break


    time.sleep(5)




