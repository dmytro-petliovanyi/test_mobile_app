from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page:

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def find_element_by_text(self, element_class: str, element_text: str, parent: bool = False) -> WebElement:
        locator = (MobileBy.XPATH, f'//{element_class}[@text="{element_text}"]')
        if parent:
            locator = (MobileBy.XPATH, f'//{element_class}[@text="{element_text}"]/..')
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_element_by_id(self, element_id: str) -> WebElement:
        locator = (MobileBy.ID, f'com.ajaxsystems:id/{element_id}')
        return self.wait.until(EC.presence_of_element_located(locator))

    @staticmethod
    def click_element(element: WebElement) -> None:
        element.click()

    @staticmethod
    def input_text(element: WebElement, text: str) -> None:
        element.send_keys(text)
