from selenium.webdriver.common.by import By
from Page_Objects.base_page import BasePage
from Test_Locators.locators import WebLocators

class LoginPage(BasePage):
    # Define locators for different elements on the page

    USERNAME = (By.NAME, WebLocators.username_text_box)
    PASSWORD = (By.NAME, WebLocators.password_text_box)

    def check_username(self):

        try:
            return self.is_visible(self.USERNAME)
        except Exception as e:
            print(f"[ERROR] Error checking Login button: {e}")
            return False

    def check_password(self):

        try:
            return self.is_visible(self.PASSWORD)
        except Exception as e:
            print(f"[ERROR] Error checking Login button: {e}")
            return False
