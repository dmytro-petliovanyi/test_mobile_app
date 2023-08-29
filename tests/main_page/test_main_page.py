from framework.main_page import MainPage
from logging_settings import logging
from tests.scripts import (assert_elements_displayed, find_elements_by_ids,
                           find_elements_by_text)


def test_main_page_add_hub_button(main_page_fixture: MainPage):
    try:
        logging.info("Starting test_main_page_add_hub_button")

        main_page = main_page_fixture
        main_page.click_add_hub_button()
        elements_info = {"Use Wizard": "android.widget.TextView",
                         "Add Manually": "android.widget.TextView"}

        assert_elements_displayed(find_elements_by_text(main_page, elements_info))

    except Exception as error:
        logging.error(error)
        raise


def test_main_page_menu_button(main_page_fixture: MainPage):
    try:
        logging.info("Starting test_main_page_menu_button")

        main_page = main_page_fixture
        main_page.click_menu_button()

        elements_ids = ["settings", "help", "logs", "camera", "addHub", "documentation_text"]

        assert_elements_displayed(find_elements_by_ids(main_page, elements_ids))

    except Exception as error:
        logging.error(error)
        raise
