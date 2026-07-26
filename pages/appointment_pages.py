from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from core.base_page import BasePage


class AppointmentPage(BasePage):

    # Appointment Form
    FACILITY = (By.ID, "combo_facility")
    READMISSION = (By.ID, "chk_hospotal_readmission")

    MEDICARE = (By.ID, "radio_program_medicare")
    MEDICAID = (By.ID, "radio_program_medicaid")
    NONE = (By.ID, "radio_program_none")

    VISIT_DATE = (By.ID, "txt_visit_date")
    COMMENT = (By.ID, "txt_comment")
    BOOK_BUTTON = (By.ID, "btn-book-appointment")

    # Confirmation Page
    CONFIRM_FACILITY = (By.ID, "facility")
    CONFIRM_PROGRAM = (By.ID, "program")
    CONFIRM_DATE = (By.ID, "visit_date")
    CONFIRM_COMMENT = (By.ID, "comment")

    def book_appointment(
        self,
        facility,
        readmission,
        healthcare_program,
        visit_date,
        comment
    ):

        Select(
            self.driver.find_element(*self.FACILITY)
        ).select_by_visible_text(facility)

        if readmission:
            self.click(self.READMISSION)

        if healthcare_program.lower() == "medicare":
            self.click(self.MEDICARE)

        elif healthcare_program.lower() == "medicaid":
            self.click(self.MEDICAID)

        else:
            self.click(self.NONE)

        self.type(self.VISIT_DATE, visit_date)
        self.type(self.COMMENT, comment)
        self.click(self.BOOK_BUTTON)

    def get_confirm_facility(self):
        return self.get_text(self.CONFIRM_FACILITY)

    def get_confirm_program(self):
        return self.get_text(self.CONFIRM_PROGRAM)

    def get_confirm_date(self):
        return self.get_text(self.CONFIRM_DATE)

    def get_confirm_comment(self):
        return self.get_text(self.CONFIRM_COMMENT)