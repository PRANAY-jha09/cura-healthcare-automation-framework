from core.driver_factor import DriverFactory
from config.config import BASE_URL


def test_framework_setup():
    driver = DriverFactory.create_driver()

    try:
        driver.get(BASE_URL)

        assert "CURA Healthcare Service" in driver.title

    finally:
        driver.quit()