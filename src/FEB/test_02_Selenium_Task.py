
import pytest
from selenium import webdriver
import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv(".env2")
import os


def test_app():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(os.getenv("URL"))

    #time.sleep(10)

    #click_btn1 = driver.find_element(By.XPATH, "//button[@id='btn-login']")
    #click_btn1.click()

    # assert "espocrm.com" in driver.current_url


   # time.sleep(10)
    #click_btn2= driver.find_element(By.XPATH,"//a[text()='Advanced Pack']")
    #click_btn2.click()

    time.sleep(10)
    xpath = "//a[@href='https://www.espocrm.com/cloud-registration/?plan=demo']"

    link = driver.find_element(By.XPATH, xpath)

    driver.execute_script("arguments[0].click();", link)
    # Wait for clickability
   # wait = WebDriverWait(driver, 10)
    #wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='https://www.espocrm.com/cloud-registration/?plan=demo']")))



    time.sleep(3)
    driver.quit()
