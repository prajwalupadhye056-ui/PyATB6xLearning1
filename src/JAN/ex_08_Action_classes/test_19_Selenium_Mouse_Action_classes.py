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



@allure.title("Actions P2")
@allure.description("Verify MouseBack")
def test_verify_action_mouse():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    atag=driver.find_element(By.ID,"click")
    atag.click()

   # ✅ If interviewer asks: “Why not Actions class?”
    # Best Answer 👇
    #
    # Selenium does not provide support for browser navigation through mouse BACK or FORWARD
    # buttons using the Actions API. Browser navigation should be handled using driver.back()
    # and driver.forward() for stability and cross-browser compatibility.
    #actions_builders=ActionBuilder(driver=driver)
    #actions_builders.pointer_action.pointer_up(MouseButton.BACK)
    #actions_builders.perform()

    driver.back()


    time.sleep(10)
    driver.quit()

