from utils.helpers import take_screenshot

def test_login_con_credenciales_invalidas(driver, login_page):
    login_page.open()
    login_page.login("usuario_invalido", "clave_incorrecta")

    error = login_page.get_error_message()

    # Guardar screenshot
    take_screenshot(driver, "login_error")

    assert error is not None
    assert "username and password do not match" in error.lower()