
import pytest
import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("App.vwo.com Implicit Wait")
@allure.description("Verify that the vwo.com is loaded with waits")
def test_negative_app_vwo_com():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    # driver.implicitly_wait(5)

    email_web_element=driver.find_element(By.ID,"login-username")
    email_web_element.send_keys("abc@gmail.com")

    password_web_element = driver.find_element(By.NAME, "password")
    password_web_element.send_keys("password@1234")

    submit_btn_web_element = driver.find_element(By.ID, "js-login-btn")
    submit_btn_web_element.click()

    #Wait for error message



    WebDriverWait(driver,timeout=3).until(EC.visibility_of_element_located((By.CLASS_NAME,"notification-box-description")))

    error_message_web_element = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_message_web_element.text)

    assert error_message_web_element.text == "Your email, password, IP address or location did not match"




