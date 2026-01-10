import allure
import time

from selenium.common import TimeoutException
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

# if webdriver try to find the element which does not exist and waited for 10sec, time out Exception will occur

@allure.title("Timeout")
@allure.description("Verify Time_out_Exception")
def test_timeout_exception_demo():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    try :
     WebDriverWait(driver=driver,timeout=10).until(EC.element_to_be_clickable((By.ID,"submit")))
     print("End of the program")


    except TimeoutException as te:
     print(te)
     print("Timeout Exception occurred!! ,10 seconds passed")
    finally:
        driver.quit()
        time.sleep(5)