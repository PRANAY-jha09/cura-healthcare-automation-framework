import pytest

from core.driver_factor import DriverFactory

@pytest.fixture
def driver():
    driver =DriverFactory.create_driver()


    yield driver
    driver.quit()
