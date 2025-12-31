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

@allure.title("Select ")
@allure.description("Verify Select Dropdown")
def test_verify_action_windows():


    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")


    select_box= driver.find_element(By.ID,"dropdown")

    select_html=Select(select_box)
    select_html.select_by_visible_text("Option 2")

    select_html.select_by_index(1)
    

    time.sleep(5)




