import pytest
import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@allure.title("Alerts")
@allure.description("Verify Alerts")
def test_alerts_js_alerts_prompt():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    element_prompt= driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']")
    element_prompt.click()

    WebDriverWait(driver=driver,timeout=5).until(EC.alert_is_present())
    alert=driver.switch_to.alert
    alert.send_keys("Prajwal")
    alert.accept()

    result_text= driver.find_element(By.ID,"result").text
    assert result_text == "You entered: Prajwal"

    time.sleep(5)

