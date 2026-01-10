import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@allure.title("SVG")
@allure.description("Verify SVG")
def test_verify_SVG():
    driver = webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")

    wait = WebDriverWait(driver, 20)

    list_of_states = driver.find_elements(By.XPATH,
                                          "//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")

    for state in list_of_states:
        print(state.get_attribute("aria-label"))

        if "Maharashtra" in state.get_attribute("aria-label"):
            state.click()
            break

    time.sleep(5)


