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

@allure.title("SVG")
@allure.description("Verify SVG")
def test_verify_action_windows():


    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")


    search= driver.find_element(By.NAME,"q")
    search.send_keys("macmini")

    list_svg_elements= driver.find_elements(By.XPATH,"//*[name()='svg']")
    list_svg_elements[0].click()
    

    time.sleep(5)




