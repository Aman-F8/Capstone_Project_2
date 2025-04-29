import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Configuration.confest import driver
from Test_Data.data import Data
from Test_Locators.locators import WebLocators


#Test-case-5:	1) Create a new user by clicking into the admin menu and verify whether the new user is able to login into the CRM or not.

def test_create_and_login_new_user(driver):
    driver.get(Data.URL)
    wait = WebDriverWait(driver, 15)

    new_username = "user_mac"
    new_password = "mac@1234"

    # Step 1: Admin Login
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, WebLocators.username_text_box))).send_keys("Admin")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, WebLocators.password_text_box))).send_keys("admin123")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, WebLocators.login_button))).click()

    # Step 2: Go to Admin → Add User
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Add ']"))).click()

    # Step 3: Fill in new user details
    # Select User Role
    wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='User Role']/../following-sibling::div"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='listbox']//span[text()='ESS']"))).click()

    # Enter Employee Name
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']"))).send_keys(
        "Peter Mac Anderson")
    time.sleep(1)  # Wait for dropdown

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@role='option']//span[contains(text(),'Peter Mac Anderson')]"))).click()

    # Enter Username
    driver.find_element(By.XPATH, "//label[text()='Username']/../following-sibling::div/input").send_keys(new_username)

    # Select Status
    driver.find_element(By.XPATH, "//label[text()='Status']/../following-sibling::div").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Enabled']"))).click()

    # Enter password & confirm password
    driver.find_element(By.XPATH, "//label[text()='Password']/../following-sibling::div/input").send_keys(new_password)
    driver.find_element(By.XPATH, "//label[text()='Confirm Password']/../following-sibling::div/input").send_keys(new_password)

    # Click Save
    driver.find_element(By.XPATH, "//button[text()=' Save ']").click()
    time.sleep(2)

    # Step 4: Logout
    wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='oxd-userdropdown-name']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))).click()

    # Step 5: Login with new user credentials
    wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys(new_username)
    driver.find_element(By.NAME, "password").send_keys(new_password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Step 6: Verify login success
    time.sleep(2)
    assert "dashboard" in driver.current_url.lower() or "dashboard" in driver.page_source.lower()
    print("\nTest Passed: New user successfully logged in.")
