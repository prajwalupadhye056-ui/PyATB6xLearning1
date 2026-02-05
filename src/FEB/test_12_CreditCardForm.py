from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time




def test_dummycreditcard():
    # Step 1: Launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://selectorshub.com/xpath-practice-page/")

    name_on_card_element= driver.find_element(By.ID,"cardName")
    name_on_card_element.send_keys("Prajwal Upadhye")

    cardnumber_element = driver.find_element(By.ID, "cardNumber")
    cardnumber_element.send_keys("8956963263668999663456678987996539653")

    entered_value = cardnumber_element.get_attribute("value")
    digits_only = entered_value.replace(" ", "")

    assert len(digits_only) == 16, (
        f"TEST FAILED: Card number must be 16 digits, but got {len(digits_only)} digits"
    )

    expiry_element = driver.find_element(By.ID, "expiry")
    expiry_element.send_keys("13/26")


    cvv_element = driver.find_element(By.ID, "cvv")
    cvv_element.send_keys("456")

    submit_element=driver.find_element(By.XPATH,"//button[@type='submit']")
    driver.execute_script("arguments[0].click();", submit_element)



    time.sleep(5)
    driver.quit()
