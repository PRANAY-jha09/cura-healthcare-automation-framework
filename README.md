
# CURA Healthcare Automation Framework

## Overview

This repository contains a QA Automation framework built using Python, Selenium, and Pytest for the CURA Healthcare demo application.
## 1. Business Overview
CURA Healthcare Service is a web-based platform designed to streamline the process of
booking medical appointments. It acts as a bridge between patients and healthcare
facilities, allowing users to schedule visits without the need for phone calls or physical visits
for booking.
## 2. Healthcare Domain
The application falls under the Healthcare IT (HealthTech) domain. Key characteristics of
this domain include:
Data Privacy: Handling sensitive patient information (though this demo uses mock data).
Accuracy: Appointment details (date, facility, program) must be precise.
Accessibility: Patients need a simple, reliable interface to manage their health schedules.

## 3. Business Workflow
The high-level business process follows this sequence:
1. Patient Authentication: User logs into the system.
2. Appointment Request: User selects a facility, healthcare program, and date.
3. Confirmation: The system generates a summary of the booked appointment.
4. Record Keeping: The appointment is stored in the user's history for future reference.
## 4. User Journey
A typical user journey (the "Happy Path") looks like this:
Landing: User visits the homepage.
Login: User enters credentials (e.g., John Doe / ThisIsNotAPassword).
Booking: User fills the "Make Appointment" form
Review: User verifies the "Appointment Confirmation" page.
History Check: User navigates to "History" to see the recorded appointment.
Exit: User logs out.
## 5. Modules
The application is organized into three primary modules:
1. Authentication Module: Handles Login and Logout.
2. Appointment Module: Handles the creation and confirmation of medical visits.
3. Profile/History Module: Manages user records and session information


## Objectives

- Learn Selenium with Python
- Practice the Page Object Model (POM)
- Build a reusable automation framework
- Perform manual and automated testing
- Showcase a QA Automation portfolio project

## Tech Stack

- Python
- Selenium
- Pytest
- Git
- GitHub

---

## Framework Components

- Driver Factory
- Configuration Loader
- Base Page
- Selenium
- Pytest

## 📝 Manual Testing Documents

The project contains manual testing documents including:

- Test Plan
- Test Cases
- Bug Report
- RTM (Requirement Traceability Matrix)

Location:

manual-testing/

---

## 🤖 Automation Framework

Framework Features:

- Page Object Model (POM)
- Reusable utility methods
- Config file support
- Screenshot capture on failure
- HTML Test Reports
- Cross-browser support (future enhancement)

Current Automated Module:

- Login

Future Modules:

- Registration
- Event Booking
- Profile Management

---

## ▶️ How to Run Tests

### 1. Clone Repository

```bash
git clone <repository-url>
```

### 2. Navigate to Project

```bash
cd eventhub-automation-framework
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Tests

```bash
pytest
```

### 5. Generate HTML Report

```bash
pytest --html=reports/report.html
```

---
## 📂 Project Structure

```text
cura_automation/
│
├── venv/                              # Python virtual environment
│
├── config/
│   ├── config.ini                     # Environment configuration
│   └── test_data.json                 # Test data (Optional)
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── home_page.py
│   ├── appointment_page.py
│   ├── history_page.py
│   └── logout_page.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_make_appointment.py
│   ├── test_appointment_history.py
│   ├── test_logout.py
│   └── test_negative_login.py
│
├── utilities/
│   ├── __init__.py
│   ├── driver_factory.py
│   ├── config_reader.py
│   ├── logger.py
│   ├── wait_utils.py
│   ├── screenshot_utility.py
│   ├── random_data.py
│   └── excel_reader.py
│
├── reports/
│   ├── report.html
│   ├── logs/
│   │   └── automation.log
│   └── screenshots/
│
├── requirements.txt
├── pytest.ini
├── README.md
├── .gitignore
└── run_tests.bat
```

---

## 👤 Author

Pranay Jha

BCA Student | QA Automation Engineer (Python)




