import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_Data.data import Data
from Test_Locators.locators import WebLocators
from Test_Data.excel_data import ExcelReader
from Configuration.confest import driver


'''
Test-case-01:
    1) Create an excel file which will comprise of following as given below.
    2) Using DDTF your verify whether the login is successful or not given username and password. After successful login logout from the CRM.
	3) Using cookies only verify whether login is successful or not
'''
@pytest.mark.usefixtures("driver")
def test_login_and_cookie_verification(driver):
    # Open the target URL in the web browser
    driver.get(Data.URL)

    # Create an ExcelReader instance to read login credentials from the Excel file
    excel_reader = ExcelReader(Data.EXCEL_FILE, Data.SHEET_NUMBER)

    # Get the total number of rows (i.e., how many user credentials to test)
    rows = excel_reader.row_count()

    # Iterate over each row of user credentials starting from row 2
    for row in range(2, rows + 1):
        # Read and strip the username and password from the respective columns
        username = excel_reader.read_data(row, 6).strip()
        password = excel_reader.read_data(row, 7).strip()

        try:
            # Wait for the username text box to be visible and input the username
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, WebLocators.username_text_box))).send_keys(username)

            # Wait for the password text box to be visible and input the password
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, WebLocators.password_text_box))).send_keys(password)

            # Wait for the login button to be clickable and click it
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, WebLocators.login_button))).click()

            # Wait until the URL contains "/dashboard" after login
            WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))

            # Check if the current URL is the expected dashboard URL
            if Data.DASHBOARD_URL in driver.current_url:
                print(f"PASSED            Login success for: {username}")
                # Mark the test as passed in the Excel file
                excel_reader.write_data(row, 8, "Test Passed")

                # Retrieve cookies from the successful session
                cookies = driver.get_cookies()

                # Begin logout process by clicking on user dropdown
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, WebLocators.user_dropdown))).click()
                # Click on the logout option
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, WebLocators.logout))).click()
                # Wait until redirected to login page after logout
                WebDriverWait(driver, 5).until(EC.url_contains("/auth/login"))

                # Clear current cookies for a fresh session
                driver.delete_all_cookies()
                # Navigate back to login page
                driver.get(Data.URL)

                # Add previously saved cookies to the browser session
                for cookie in cookies:
                    # Remove "sameSite" attribute if present to avoid errors
                    cookie.pop("sameSite", None)
                    driver.add_cookie(cookie)

                # Navigate directly to dashboard to test cookie-based login
                driver.get(Data.DASHBOARD_URL)
                try:
                    # Wait until redirected to dashboard
                    WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))
                    # If successful, mark cookie login as verified
                    if Data.DASHBOARD_URL in driver.current_url:
                        print(f"Cookie login verified for {username}")
                        excel_reader.write_data(row, 9, "Cookie Login Verified")
                    else:
                        # If redirected elsewhere, raise an error
                        raise Exception("Redirected elsewhere")
                except:
                    # Cookie-based login failed
                    print(f"Cookie login failed for {username}")

            else:
                # Login was unsuccessful
                print(f"FAILED            Test failed for username={username}")
                # Mark the test as failed in the Excel file
                excel_reader.write_data(row, 8, "Test Failed")

            # Reset to login page before next iteration
            driver.get(Data.URL)

        except Exception as e:
            # Catch-all for any unexpected exception during test
            print(f"FAILED            Test failed for username={username}")
            # Log the failure in the Excel file
            excel_reader.write_data(row, 8, "Test Failed")
            # Reset to login page before next test
            driver.get(Data.URL)

