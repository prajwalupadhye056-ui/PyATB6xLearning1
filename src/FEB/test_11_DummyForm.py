from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dummyform():
    # Step 1: Launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://selectorshub.com/xpath-practice-page/")

    email_element= driver.find_element(By.XPATH,"//input[@type='email']")
    email_element.send_keys("prajwal.upadhye056@gmail.com")

    wait = WebDriverWait(driver, 10)

    password = wait.until(
        EC.element_to_be_clickable((By.ID, "pass"))
    )

    password.send_keys("Test@123")

    name_element=driver.find_element(By.NAME,"company")
    name_element.send_keys("ABC Pvt Ltd")

    mobile_element = driver.find_element(By.NAME, "mobile number")
    mobile_element.send_keys("963562398")

    country_element=driver.find_element(By.XPATH, "//label[contains(text(),'Country')]//input")
    country_element.send_keys("India")




    time.sleep(5)
    driver.quit()
