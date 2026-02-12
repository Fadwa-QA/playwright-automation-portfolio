from pages.login_page import LoginPage
from pages.success_page import SuccessPage

def test_login_success(page):
    login = LoginPage(page)
    success = SuccessPage(page)

    login.open()
    login.login("student", "Password123")

    success.wait_loaded()
    assert success.is_loaded()
