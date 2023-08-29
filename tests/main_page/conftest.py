from typing import Any, Generator

import pytest

from framework.main_page import MainPage


@pytest.fixture(scope='function')
def main_page_fixture(driver) -> Generator[MainPage, Any, None]:
    yield MainPage(driver)
