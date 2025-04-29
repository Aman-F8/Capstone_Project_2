# OrangeHRM Login Automation Framework

## 🚀 Project Title
**Mini Project 02: Automated Testing of OrangeHRM Web Application**

## 🔗 Live Test URL
[https://opensource-demo.orangehrmlive.com/web/index.php/auth/login](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)

## 📌 Objective
The objective of this mini project is to design and develop a robust test automation framework using **Python**, **Selenium**, **Pytest**, and **Page Object Model (POM)**. The framework automates end-to-end testing of the OrangeHRM demo application, including login, logout, menu visibility, user creation, and data-driven validation using **Excel**.

## 🧰 Tools & Technologies Used
- Python (OOPS and Exception Handling)
- Selenium WebDriver
- Pytest (for test execution and HTML report generation)
- Page Object Model (POM)
- Data-Driven Testing Framework (DDFT) using Excel
- Keyword-Driven Testing Framework (KDTF) using YAML
- Explicit Waits
- HTML Reporting with `pytest-html`
- Pylint for code quality and naming conventions


## ✅ Test Suite Summary

### 🔹 Test Case 1:
- Validate login using DDT from Excel file.
- Validate login using cookies.
- Logout functionality.
- ✅ **HTML report generated**

### 🔹 Test Case 2:
- Verify if the home URL is working and accessible.
- ✅ **HTML report generated**

### 🔹 Test Case 3:
- Verify visibility of username and password input fields.
- ✅ **HTML report generated**

### 🔹 Test Case 4:
- After login, check if the menus (Admin, PIM, Leave, Time, Recruitment, My Info, Performance, Dashboard) are visible and clickable.
- ✅ **HTML report generated**

### 🔹 Test Case 5:
- Create a new user using Admin panel and verify if the new user can login successfully.
- ✅ **HTML report generated**

### 🔹 Test Case 6:
- From Admin menu, verify if the newly created user exists in the records.
- ✅ **HTML report generated**

## ⚙️ Features
- Supports multiple browsers: Chrome, Edge, Firefox
- Modular POM structure with reusable page methods
- Follows Pylint naming and style guidelines
- Data-driven testing from Excel
- Keyword-driven testing from YAML
- Explicit waits for stability
- Custom error handling
- Pytest HTML reports
- Automatically closes browser post-execution



