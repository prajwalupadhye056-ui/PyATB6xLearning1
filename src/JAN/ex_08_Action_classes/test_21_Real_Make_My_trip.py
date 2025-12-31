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

@allure.title("Make my trip automation ")
@allure.description("Verify make my trip automation using action classes")
def test_verify_action_makemytrip():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()

    WebDriverWait(driver=driver,timeout=5).until(EC.visibility_of_element_located((By.XPATH,"//span[@data-cy='closeModal']")))

    driver.find_element(By.XPATH,"//span[@data-cy='closeModal']").click()
    time.sleep(2)

    fromCity=driver.find_element(By.ID,"fromCity")

    action=ActionChains(driver=driver)
    action.move_to_element(fromCity).click().send_keys("del").perform()

    time.sleep(2)
    action.move_to_element(fromCity).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()


    allure.attach(driver.get_screenshot_as_png(),name="test_verify_action_makemytrip"
                  ,attachment_type=AttachmentType.PNG)
