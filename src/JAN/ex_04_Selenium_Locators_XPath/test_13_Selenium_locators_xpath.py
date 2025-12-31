import driver
import pytest
from selenium import webdriver
import allure
import time
from selenium.webdriver.common.by import By


@allure.title("VWO Login Negative Testcase")
@allure.description("TC1 - Negative TC - VWO Login with Invalid cred.")
@pytest.mark.negativevwologin
def test_app_vwo_login_chrome():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_app_btn= driver.find_element(By.XPATH,"//a[text()='Make Appointment']")
    make_app_btn.click()
    time.sleep(10)
    driver.quit()
