from pages.login_page import LoginPage

def test_login_empty_password(page):
    login = LoginPage(page)
    login.open()
    login.login("student", "")

    msg = login.error_message()
    assert "invalid" in msg.lower()

def test_login_empty_username(page):
    login = LoginPage(page)
    login.open()
    login.login("", "Password123")

    msg = login.error_message()
    assert "invalid" in msg.lower()
