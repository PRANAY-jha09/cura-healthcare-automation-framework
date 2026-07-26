from selenium.webdriver.common.by import By
from core.base_page  import BasePage


class LoginPage(BasePage):

    MAKE_APPOINTMENT_BTN = (By.ID, "btn-make-appointment")
    USERNAME = (By.ID, "txt-username")
    PASSWORD = (By.ID, "txt-password")
    LOGIN_BTN = (By.ID, "btn-login")
    MENU = (By.ID, "menu-toggle")
    LOGOUT = (By.LINK_TEXT, "Logout")

    def open_login_page(self, base_url):
        self.driver.get(base_url)
        self.driver.find_element(*self.MAKE_APPOINTMENT_BTN).click()

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()

    def logout(self):
        self.driver.find_element(*self.MENU).click()
        self.driver.find_element(*self.LOGOUT).click()