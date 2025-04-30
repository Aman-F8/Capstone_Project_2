# MINI-PROJECT-02: OrangeHRM Web Automation Using Python Selenium & Pytest

**Title:**  
Automating the demo CRM web application [OrangeHRM](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login) using **Python Selenium**, **Pytest**, **POM**, **DDT**, and **Keyword-Driven Hybrid Testing**.

---

## Project Summary

This mini-project automates the functional testing of the OrangeHRM demo CRM web application using a hybrid automation framework built on **Python Selenium** and **Pytest**. The framework follows the **Page Object Model (POM)** structure, leverages **Object-Oriented Programming (OOP)** principles, and implements **Data-Driven Testing (DDT)** using Excel. The automation suite includes login verification, user creation, and menu validations—across both positive and negative test scenarios. Explicit waits ensure stability, while **Pytest HTML reports** provide detailed test execution results.

---

## Test Objective

Build a system to automatically verify the functionality of the OrangeHRM demo web app using a **modular, scalable, and maintainable automation framework**. The system will:
- Navigate and interact with the web application across multiple browsers.
- Validate expected elements and behaviors.
- Leverage cookies for login session verification.
- Generate structured test reports.

---

## Tools and Technologies

- **Python 3**
- **Selenium WebDriver**
- **Pytest**
- **Page Object Model (POM)**
- **Data-Driven Testing (DDT)** using Excel
- **Keyword-Driven + Hybrid Testing**
- **Explicit Waits**
- **Pytest HTML Reporting**
- **Pylint** (for Python naming conventions and code quality)

---

## Target URL

> [https://opensource-demo.orangehrmlive.com/web/index.php/auth/login](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)

---

## Precondition

All test cases are written for **both positive and negative scenarios**, adhering strictly to **POM**, **OOP**, and **DDT** principles.

---

## Test Suite

### **Test Case 01: DDT Login and Cookie Validation**
1. Create an **Excel file** with login credentials (username and password).
2. Using **Data-Driven Testing**, verify whether the login is successful.
3. After a successful login, perform logout.
4. Use **cookies only** to verify successful login.
5. Generate **pytest-based HTML report**.

---

### **Test Case 02: Home URL Validation**
1. Verify if the **home/login page URL** loads successfully.
2. Generate **pytest-based HTML report**.

---

### **Test Case 03: Input Fields Visibility**
1. Verify that **username and password input fields** are visible.
2. Generate **pytest-based HTML report**.

---

### **Test Case 04: Post-Login Menu Validation**
1. After a valid login, verify that the following menus are **visible and clickable**:
   - Admin
   - PIM
   - Leave
   - Time
   - Recruitment
   - My Info
   - Performance
   - Dashboard
2. Generate **pytest-based HTML report**.

---

### **Test Case 05: New User Creation & Login**
1. Go to **Admin** menu and create a **new user**.
2. Verify that the **new user is able to login** successfully.
3. Generate **pytest-based HTML report**.

---

### **Test Case 06: Verify New User in Admin Records**
1. From the **Admin menu**, verify that the **new user exists in the user list**.
2. Generate **pytest-based HTML report**.

---
