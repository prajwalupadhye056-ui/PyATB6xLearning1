import driver
import pytest
from selenium import webdriver
import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_Katalon_chrome():

    chrome_options= Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--window-size=900,600")
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(10)
    driver.quit()

