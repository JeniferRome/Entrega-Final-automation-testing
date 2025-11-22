import pytest
from page.login_page import LoginPage
from data.data_login import CASOS_LOGIN
from utils.example_cvs import get_login_csv
from utils.faker import get_login_faker


@pytest.mark.parametrize("username,password,login_bool", get_login_faker())
def test_login( driver, username, password, login_bool ):
    #crear objeto (instanciarlo)
    loginPage = LoginPage(driver)
    loginPage.open()
    loginPage.login(username, password)


    if login_bool:
       assert "inventory.html" in driver.current_url
    else:
       assert "inventory.html" not in driver.current_url


   