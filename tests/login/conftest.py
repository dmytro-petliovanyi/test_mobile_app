import os
from typing import Any, Generator

import pytest

from framework.login_page import LoginPage

valid_email = os.environ["QA_DEVELOPER_EMAIL"]
valid_password = os.environ["QA_DEVELOPER_PASSWORD"]
invalid_email = "invalid_email"
invalid_password = "invalid_password"
invalid_email_right_template = "some@gmail.com"


@pytest.fixture(scope='function')
def user_login_fixture(driver) -> Generator[LoginPage, Any, None]:
    yield LoginPage(driver)
