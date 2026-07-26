from core.driver_factor import DriverFactory
from config.config import BASE_URL
from pages.login_page import LoginPage
from pages.appointment_pages import AppointmentPage

def test_book_appointment():
    driver =DriverFactory.create_driver()

    try:
        login =LoginPage(driver)
        appointment=AppointmentPage(driver)

        login.open_login_page(BASE_URL)

        login.login(
            "John Doe",
            "ThisIsNotAPassword"
        )
        appointment.book_appointment(
            facility ="Tokyo CURA Healthcare Center",
            readmission =True,
            healthcare_program ="Medicaid",
            visit_date ="30/12/2026",
            comment="Automation Test"
        )
        assert "Appointment Confirmation" in driver.page_source

    finally:
        driver.quit()