from core.driver_factor import DriverFactory
from config.config import BASE_URL
from pages.login_page import LoginPage


def test_invalid_login():
    driver =DriverFactory.create_driver()

    try:
        login =LoginPage(driver)
        login.open_login_page(BASE_URL)

        login.login(
            "WrongUser",
            "WrongPassword"
        )

        assert "Login failed" in driver.page_source

    finally:
        driver.quit()
