import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Configuration.confest import driver
from Test_Data.data import Data
from Test_Locators.locators import WebLocators


# Test-case-6:	1) Verify from the admin menu that the new user exists in the record of the users or not.

def test_verify_new_user_exists(driver):
    driver.get(Data.URL)
    wait = WebDriverWait(driver, 15)
    new_username = "user_mac"

    # Step 1: Admin Login

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, WebLocators.username_text_box))).send_keys("Admin")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, WebLocators.password_text_box))).send_keys("admin123")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, WebLocators.login_button))).click()

    # Step 2: Navigate to Admin menu
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']"))).click()

    # Step 3: Enter username in the search field
    username_input = wait.until(EC.visibility_of_element_located((
        By.XPATH, "//label[text()='Username']/../following-sibling::div/input"
    )))
    username_input.send_keys(new_username)

    # Step 4: Click Search
    driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()

    # Step 5: Wait and verify the user appears in results
    time.sleep(2)  # Let table reload
    rows = driver.find_elements(By.XPATH, "//div[@role='table']//div[@role='row']")

    user_found = False
    for row in rows[1:]:  # skip header row
        if new_username in row.text:
            user_found = True
            break

    assert user_found, f"User '{new_username}' was not found in the user records."
    print(f"\nTest Passed: User '{new_username}' exists in Admin > User Management.")
