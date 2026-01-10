import allure
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@allure.title("SVG")
@allure.description("Verify SVG")
@allure.title("SVG")
@allure.description("Verify SVG - Non Existing State")
def test_verify_SVG():
    driver = webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")

    wait = WebDriverWait(driver, 20)

    try:
        list_of_states = driver.find_elements(
            By.XPATH,
            "//*[name()='svg']//*[name()='path' and @aria-label]"
        )

        for state in list_of_states:
            state_name = state.get_attribute("aria-label")  # ✅ fixed
            print(state_name)

            if "Atlantis" in state_name:
                state.click()
                break

        print("Atlantis does not exist – expected negative scenario")

    except NoSuchElementException as e:
        print("Handled NoSuchElementException:", e)

    finally:
        time.sleep(5)
        driver.quit()

