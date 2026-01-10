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


# If we are trying to find the element which does not exist NoSuchElementException will occur


@allure.title("exception_handle")
@allure.description("Verify exception_handle")
def test_exception_handle():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    try :
       element = driver.find_element(By.XPATH,"this_id_doesnt exist")

    except NoSuchElementException as nse:
     print(nse.msg)




