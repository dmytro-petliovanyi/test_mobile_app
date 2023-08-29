import time

import pytest

from framework.login_page import LoginPage
from logging_settings import logging
from tests.login.conftest import (invalid_email, invalid_email_right_template,
                                  invalid_password, valid_email,
                                  valid_password)
from tests.scripts import assert_elements_displayed, find_elements_by_ids


def test_user_login_positive_case(user_login_fixture: LoginPage):
    try:
        logging.info("Starting test_user_login_positive_case")
        login_page = user_login_fixture

        login_page.click_login_button()

        login_page.enter_email(valid_email)
        login_page.enter_password(valid_password)
        login_page.click_login_button()
        elements_ids = ["menuDrawer", "hubAdd"]

        assert_elements_displayed(find_elements_by_ids(login_page, elements_ids))

        driver = login_page.driver
        driver.close_app()
        time.sleep(1)
        driver.launch_app()
        time.sleep(1)
        logging.info("Ending test_user_login_positive_case")

    except Exception as error:
        logging.error(error)
        raise


@pytest.mark.parametrize(
    "email,password,expected", [
        (
            invalid_email, invalid_password, "Invalid email format"
        ),
        (
            invalid_email_right_template, valid_password, "Wrong login or password"
        ),
        (
            valid_email, invalid_password, "Wrong login or password"
        )
    ]
)
def test_user_login_negative_case(user_login_fixture: LoginPage, email: str, password: str, expected: str):
    try:
        login_page = user_login_fixture

        logging.info(f"Starting test with email: '{email}', password: '{password}'")

        login_page.click_login_button()

        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_login_button()

        error_message = login_page.get_error_message()

        if not error_message == expected:
            logging.error(f"Expected error message: '{expected}', but got: '{error_message}'")
            raise AssertionError("Message mismatch")

        login_page.navigate_back()

        time.sleep(2)

        logging.info(f'Test completed for email: "{email}", password: "{password}"')
    except Exception as error:
        logging.error(error)
        raise
