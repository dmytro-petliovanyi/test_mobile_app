from framework.main_page import MainPage
from logging_settings import logging


def test_main_page_add_hub_button(main_page_fixture: MainPage):
    try:
        logging.info("Starting test_user_login_positive_case")

        main_page = main_page_fixture
        main_page.click_add_hub_button()

        use_wizard_element = main_page.find_element_by_text("android.widget.TextView", "Use Wizard")
        add_manually_element = main_page.find_element_by_text("android.widget.TextView", "Add Manually")

        if not all([use_wizard_element.is_displayed(), add_manually_element.is_displayed()]):
            logging.error("Dashboard element not found")
            raise AssertionError("Dashboard element not found")

    except Exception as error:
        logging.error(error)
        raise


def test_main_page_menu_button(main_page_fixture: MainPage):
    try:
        logging.info("Starting test_user_login_positive_case")

        main_page = main_page_fixture
        main_page.click_menu_button()

        app_settings_element = main_page.find_element_by_id("settings")
        help_element = main_page.find_element_by_id("help")
        report_a_problem_element = main_page.find_element_by_id("logs")
        video_surveillance_element = main_page.find_element_by_id("camera")
        add_hub_element = main_page.find_element_by_id("addHub")
        terms_of_service_element = main_page.find_element_by_id("documentation_text")

        if not all([
            app_settings_element.is_displayed(),
            help_element.is_displayed(),
            report_a_problem_element.is_displayed(),
            video_surveillance_element.is_displayed(),
            add_hub_element.is_displayed(),
            terms_of_service_element.is_displayed()
        ]):
            logging.error("Dashboard element not found")
            raise AssertionError("Dashboard element not found")

    except Exception as error:
        logging.error(error)
        raise
