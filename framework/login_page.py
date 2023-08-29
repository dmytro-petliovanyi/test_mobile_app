from appium.webdriver.webdriver import WebDriver

from .page import Page


class LoginPage(Page):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def enter_email(self, email: str) -> None:
        email_label = self.find_element_by_text('android.widget.TextView', 'Email', True)
        self.click_element(email_label)
        self.input_text(email_label, email)

    def enter_password(self, password: str) -> None:
        password_field = self.find_element_by_text('android.widget.TextView', 'Password', True)
        self.click_element(password_field)
        self.input_text(password_field, password)

    def click_login_button(self) -> None:
        login_button = self.find_element_by_text('android.widget.TextView', 'Log In')
        self.click_element(login_button)

    def get_error_message(self) -> str:
        error_element = self.find_element_by_id("snackbar_text")
        return error_element.text

    def navigate_back(self) -> None:
        back_button = self.find_element_by_id("back")
        self.click_element(back_button)
