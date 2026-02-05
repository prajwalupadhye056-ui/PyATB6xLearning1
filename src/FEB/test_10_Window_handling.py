# Verify that on this URL, when a person click on the click here button,
# it opens a new window. Where a new window is written, you have to verify that also.
# the-internet.herokuapp.com/windows
# You have to open the URL which I am going to give you. # You need to basically,
# from the parent page, click on the "Click Here" button. # The moment you click on that
# button, it will open a child page, which is another tab. # You need to switch to that
# tab and verify that there is a particular text available # on the page source - yes or no.
# Then, if you want, you can switch back to the parent as well.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_window():
    # Step 1: Launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Step 2: Open the URL
        driver.get("https://the-internet.herokuapp.com/windows")

        # Store parent window handle
        parent_window = driver.current_window_handle

        # Step 3: Click on "Click Here"
        driver.find_element(By.LINK_TEXT, "Click Here").click()

        # Step 4: Get all window handles
        window_handles = driver.window_handles

        # Step 5: Switch to child window
        for handle in window_handles:
            if handle != parent_window:
                driver.switch_to.window(handle)
                break

        # Step 6: Verify text in child window
        if "New Window" in driver.page_source:
            print("PASS: 'New Window' text is present in child window")
            assert True
        else:
            print("FAIL: 'New Window' text is NOT present")
            assert False

        # Step 7 (Optional): Switch back to parent window
        driver.switch_to.window(parent_window)

    finally:
        # Step 8: Close browser
        time.sleep(2)
        driver.quit()
