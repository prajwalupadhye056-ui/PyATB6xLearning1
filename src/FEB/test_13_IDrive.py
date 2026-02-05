from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_iDrive360():
    # Step 1: Launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()



    driver.get("https://www.idrive360.com/enterprise/login")

    wait = WebDriverWait(driver, 10)

    email = wait.until(
        EC.visibility_of_element_located((By.ID, "email"))
    )

    email.send_keys("augtest_040823@idrive.com")



    password_element = driver.find_element(By.ID, "password")
    password_element.send_keys("123456")

    remember_me=driver.find_element(By.XPATH,"//span[contains(@class,'id-checkmark')]")

    remember_me.click()
