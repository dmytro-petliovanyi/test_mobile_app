import pytest

from framework.menu import Menu
from logging_settings import logging
from tests.scripts import assert_elements_displayed, find_elements_by_text


@pytest.mark.parametrize(
    "button_text, elements_info", [
        ("App Settings", {
            "Edit Account": "android.widget.TextView",
            "Sessions": "android.widget.TextView",
            "Account Protection": "android.widget.TextView",
            "System Settings": "android.widget.TextView"
        }),
        ("Help", {
            "Installation Manuals": "android.widget.TextView"
        }),
        ("Report a Problem", {
            "Report a Problem": "android.widget.TextView",
            "Delete": "android.widget.TextView"
        }),
        ("Video Surveillance", {
            "Video Surveillance": "android.widget.TextView",
            "Hikvision/Safire": "android.widget.TextView",
            "Uniview": "android.widget.TextView"
        })
    ]
)
def test_menu_buttons(menu_page_fixture: Menu, button_text: str, elements_info: dict):
    try:
        logging.info(f"Starting test_{button_text.replace(' ', '_').lower()}_button")

        menu_page = menu_page_fixture
        click_method_name = f"click_{button_text.replace(' ', '_').lower()}_button"
        click_method = getattr(menu_page, click_method_name)
        click_method()

        assert_elements_displayed(find_elements_by_text(menu_page, elements_info))

    except Exception as error:
        logging.error(error)
        raise


def test_menu_add_hub_button(menu_page_fixture: Menu):
    try:
        logging.info("Starting test_menu_add_hub_button")

        menu_page = menu_page_fixture
        menu_page.click_add_hub_button()
        elements_info = {"Use Wizard": "android.widget.TextView",
                         "Add Manually": "android.widget.TextView"}

        assert_elements_displayed(find_elements_by_text(menu_page, elements_info))

    except Exception as error:
        logging.error(error)
        raise


def test_menu_terms_of_service_button(menu_page_fixture: Menu):
    try:
        logging.info("Starting test_menu_terms_of_service_button")

        menu_page = menu_page_fixture
        menu_page.click_terms_of_service_button()
        elements_info = {"Terms of Service": "android.widget.TextView",
                         "End User Agreement": "android.widget.TextView",
                         "Privacy Policy": "android.widget.TextView",
                         "Privacy Notice": "android.widget.TextView"}

        assert_elements_displayed(find_elements_by_text(menu_page, elements_info))

    except Exception as error:
        logging.error(error)
        raise
