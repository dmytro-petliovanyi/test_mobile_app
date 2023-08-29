from appium.webdriver.webdriver import WebDriver

from framework.page import Page


class MainPage(Page):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def click_menu_button(self) -> None:
        menu_button = self.find_element_by_id('menuDrawer')
        self.click_element(menu_button)

    def click_add_hub_button(self) -> None:
        add_hub_button = self.find_element_by_id('hubAdd')
        self.click_element(add_hub_button)
