import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_account_registration():

    driver = webdriver.Chrome()
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    # Step 1: Navigate to Registration Page
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

    # Step 2: Fill Registration Form
    driver.find_element(By.ID, "input-firstname").send_keys("Prajwal")
    driver.find_element(By.ID, "input-lastname").send_keys("Upadhye")

    # Generate unique email every time
    email = f"prajwal{random.randint(1000, 9999)}@test.com"
    driver.find_element(By.ID, "input-email").send_keys(email)

    driver.find_element(By.ID, "input-telephone").send_keys("9999999999")
    driver.find_element(By.ID, "input-password").send_keys("Test@123")
    driver.find_element(By.ID, "input-confirm").send_keys("Test@123")

    # Step 3: Select Newsletter (No)
    driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='0']").click()

    # Step 4: Accept Privacy Policy
    driver.find_element(By.NAME, "agree").click()

    # Step 5: Click Continue
    driver.find_element(By.XPATH, "//input[@value='Continue']").click()

    # Step 6: Verify Success Message
    success_msg = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h1[text()='Your Account Has Been Created!']")
        )
    )

    assert success_msg.text == "Your Account Has Been Created!"
    print("✅ Test Passed: Account successfully created")

    time.sleep(10)
    driver.quit()











