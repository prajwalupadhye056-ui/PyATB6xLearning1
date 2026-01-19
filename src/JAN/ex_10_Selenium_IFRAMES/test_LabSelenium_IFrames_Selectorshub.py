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

@allure.title("Selenium_IFRAMES")
@allure.description("Verify IFRAMES")
def test_verify_windows():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://selectorshub.com/iframe-scenario/")
    driver.maximize_window()

    driver.switch_to.frame("pact1")

    crush_finder_input_box=driver.find_element(By.XPATH,"//input[@id='inp_val']")
    crush_finder_input_box.send_keys("Prrraajwal")

    driver.switch_to.frame("pact2")

    jax_input_box = driver.find_element(By.XPATH, "//input[@id='jax']")
    crush_finder_input_box.send_keys("Upadhye")


    #Switch to parent using default-content
    driver.switch_to.default_content()
    driver.switch_to.frame("pact1")

    crush_finder_input_box = driver.find_element(By.XPATH, "//input[@id='inp_val']")
    crush_finder_input_box.clear()
    crush_finder_input_box.send_keys("Lucky")

    time.sleep(5)

