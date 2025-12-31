import pytest
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

@allure.title("Actions P3")
@allure.description("Verify Click and Hold")
def test_verify_action_mouse():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    #draggable

    elements_to_hold= driver.find_element(By.ID,"draggable")


    #KEY DOWN

    actions=ActionChains(driver)
    actions.click_and_hold(on_element=elements_to_hold).perform()

    time.sleep(10)
    driver.quit()