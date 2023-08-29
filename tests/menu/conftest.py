from typing import Any, Generator

import pytest

from framework.menu import Menu


@pytest.fixture(scope='function')
def menu_fixture(driver) -> Generator[Menu, Any, None]:
    yield Menu(driver)
