from pages.login_page import LoginPage
from pages.success_page import SuccessPage

def test_logout(page):
    login = LoginPage(page)
    success = SuccessPage(page)

    login.open()
    login.login("student", "Password123")

    success.wait_loaded()
    success.logout()

    page.wait_for_selector("#username", timeout=60000)
    assert "practice-test-login" in page.url
