# Bug Report

## Bug ID

BUG-001

---

## Title

Login page allows user to click the Login button with empty username and password.

---

## Module

Login

---

## Severity

Medium

---

## Priority

High

---

## Environment

- Application: CURA Healthcare Service Demo
- URL: https://katalon-demo-cura.herokuapp.com/
- Browser: Chrome 138
- OS: Windows 11

---

## Preconditions

User is on the Login page.

---

## Steps to Reproduce

1. Open the application.
2. Click **Make Appointment**.
3. Leave the Username field empty.
4. Leave the Password field empty.
5. Click **Login**.

---

## Expected Result

The application should display validation messages such as:

- Username is required.
- Password is required.

The login request should not be submitted.

---

## Actual Result

The application accepts the Login button click and does not display field-level validation messages.

---

## Test Data

Username: (Blank)

Password: (Blank)

---

## Attachment

Screenshot: Not Attached

---

## Status

Open

---

## Reported By

Pranay Jha

---

## Reported Date

24-Jul-2026 

----------------------------------------------------------------------------------------------------------------------
