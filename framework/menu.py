from appium.webdriver.webdriver import WebDriver

from framework.page import Page


class Menu(Page):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def click_add_hub_button(self) -> None:
        add_hub_button = self.find_element_by_id('hubAdd')
        self.click_element(add_hub_button)

    def click_app_settings_button(self) -> None:
        settings_button = self.find_element_by_id('settings')
        self.click_element(settings_button)

    def click_help_button(self) -> None:
        help_button = self.find_element_by_id('help')
        self.click_element(help_button)

    def click_report_a_problem_button(self) -> None:
        report_a_problem_button = self.find_element_by_id('logs')
        self.click_element(report_a_problem_button)

    def click_terms_of_service_button(self) -> None:
        terms_of_service_button = self.find_element_by_id('documentation_text')
        self.click_element(terms_of_service_button)
