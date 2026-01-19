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
    driver.get("https://the-internet.herokuapp.com/iframe")
    driver.maximize_window()

    driver.switch_to.frame("mce_0_ifr")

    p_text=driver.find_element(By.XPATH,"//body[@id='tinymce']/p")
    print(p_text.text)
    assert "Your content goes here." in p_text.text