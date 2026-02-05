from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_firstcry_product_details():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.firstcry.com/")

    wait = WebDriverWait(driver, 30)


    footwear_menu = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Footwear']"))
    )
    actions=ActionChains(driver=driver)
    actions.move_to_element(footwear_menu).perform()


    for sandal in driver.find_elements(By.XPATH, "//a[@title='Sandals']"):
        if sandal.is_displayed():
            sandal.click()
            break


    product_title = "Cute Walk by Babyhug Velcro Closure Sandals with Floral Print - Pink"
    product_img = wait.until(EC.visibility_of_element_located((By.XPATH, f"//img[@title='{product_title}']")))

    driver.execute_script("arguments[0].scrollIntoView(true);", product_img)
    driver.execute_script("arguments[0].click();", product_img)

    parent = driver.current_window_handle
    wait.until(lambda d: len(d.window_handles) > 1)

    for handle in driver.window_handles:
        if handle != parent:
            driver.switch_to.window(handle)
            break

    time.sleep(2)  # allow page to load fully



    # MRP
    mrp_elem = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(@class,'prod-price')]")))
    mrp = mrp_elem.get_attribute("data-price")
    print("MRP:", mrp)

    driver.quit()
