from appium.webdriver import WebElement

from framework.page import Page
from logging_settings import logging


def assert_elements_displayed(elements: list[WebElement]) -> None:
    for element in elements:
        if not element.is_displayed():
            logging.error("Dashboard element not found")
            raise AssertionError("Dashboard element not found")


def find_elements_by_ids(page: Page, elements_ids: list[str]) -> list[WebElement]:
    return [page.find_element_by_id(element_id) for element_id in elements_ids]


def find_elements_by_text(page: Page, elements_info: dict[str, str]) -> list[WebElement]:
    return [page.find_element_by_text(value, key) for key, value in elements_info.items()]
