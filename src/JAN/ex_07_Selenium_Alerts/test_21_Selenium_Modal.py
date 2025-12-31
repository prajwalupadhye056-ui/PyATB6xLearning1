
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
    driver.get("https://www.makemytrip.com/")

    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='commonModal__close']")))


    modal = driver.find_element(By.XPATH, "//span[@class='commonModal__close']")

    time.sleep(5)
