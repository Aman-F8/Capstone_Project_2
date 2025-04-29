import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Test_Data.data import Data
from Test_Locators.locators import WebLocators
from Configuration.confest import driver
from Page_Objects.login_page import LoginPage


# Test-case-2:	1) Verify whether the home URL is working or not.

def test_verify_home_url(driver):
    driver.get(Data.URL)
    try:
        # Wait until username field is visible (meaning login page loaded successfully)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, WebLocators.username_text_box))
        )
        assert Data.URL in driver.current_url, "URL did not match"
        print("PASSED            Home URL is accessible and loaded successfully.")
    except Exception as e:
        print("FAILED            Home URL is not accessible.")
        pytest.fail("Home URL not working: " + str(e))


# Test-case-3:	1) Verify whether the username, password input boxes are visible or not.

def test_input_box_visible(driver):

    try:
        # Open the target URL in the browser
        driver.get(Data.URL)
        login_page = LoginPage(driver)

        username_input_box = login_page.check_username()
        password_input_box = login_page.check_username()

        # assert username_input_box, "[FAIL] Login button not visible"
        # assert password_input_box, "[FAIL] Login button not visible"

        if username_input_box:
            print("[PASS] Username input box is visible.")
        else:
            print("[FAIL] Username input box is not visible.")
        assert username_input_box, "[FAIL] Username input box not visible"

        if password_input_box:
            print("[PASS] Password input box is visible.")
        else:
            print("[FAIL] Password input box is not visible.")
        assert password_input_box, "[FAIL] Password input box not visible"

    except Exception as e:
        print(f"[ERROR] Login button check failed: {e}")
        pytest.fail("Buttons are not visible")


# Test-case-4:	1) Verify after successful login, whether the menus Admin, PIM, Leave, Time
#                  Recruitment, Myinfo, Performance, Dashboard are visible and clickable or not.

def test_main_menus_visible_and_clickable(driver):
    driver.get(Data.URL)
    wait = WebDriverWait(driver, 60)

    try:
        # Login
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, WebLocators.username_text_box))).send_keys("Admin")
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, WebLocators.password_text_box))).send_keys("admin123")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, WebLocators.login_button))).click()

        # Menus to verify
        expected_menus = [
            "Admin", "PIM", "Leave", "Time",
            "Recruitment", "My Info", "Performance", "Dashboard"
        ]

        for menu_text in expected_menus:
            menu = wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{menu_text}']")))
            assert menu.is_displayed(), f" Menu '{menu_text}' is not visible"
            print(f" Menu '{menu_text}' is visible and clickable.")

    except TimeoutException as e:
        print("Test failed due to a TimeoutException.")
        assert False, f"Element not found: {str(e)}"
