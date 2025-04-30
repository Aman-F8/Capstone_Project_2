"""
Basic Locators
"""

class WebLocators:

    #Locator for this fields
    username_text_box = "username"              # This is the 'name' attribute of the username input field
    password_text_box = "password"              # This is the 'name' attribute of the password input field
    login_button = "button[type = 'submit']"    # This is a CSS selector for the submit button
    user_dropdown = "oxd-userdropdown-tab"      # This is the 'class' attribute of the user dropdown element
    logout = "//a[text()='Logout']"             # This is an XPath to find the 'Logout' link by its text

