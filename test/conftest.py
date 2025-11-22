import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)


import pytest
from utils.helpers import get_driver
from page.login_page import LoginPage

@pytest.fixture
def driver():
    # configuracion para consultar a selenium
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    # Fixture para usar el Page Object del login
    return LoginPage(driver)
