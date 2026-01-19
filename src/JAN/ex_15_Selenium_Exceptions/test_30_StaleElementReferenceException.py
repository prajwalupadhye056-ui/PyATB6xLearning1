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
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

#previous webdriver has found the element and we do driver.refresh()- StaleElementReferenceElement will occur
#Refreshment of the DOM
#DOM structure or HTML changed
@allure.title("exception_handle_SERE")
@allure.description("Verify exception_handle")
def test_stale_element_demo():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    try :
     textarea = driver.find_element(By.NAME,"q")

     driver.refresh()

     textarea.send_keys("The Testing Academy")
     print("The end of the testcase")

    except StaleElementReferenceException as see:
     print(see.msg)
    time.sleep(5)