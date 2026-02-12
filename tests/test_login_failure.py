from pages.login_page import LoginPage

def test_login_failure(page):
    login = LoginPage(page)

    login.open()
    login.login("wrong", "wrong")

    msg = login.error_message()
    assert "invalid" in msg.lower()
