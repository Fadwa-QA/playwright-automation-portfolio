class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://practicetestautomation.com/practice-test-login/"

        self.username = "#username"
        self.password = "#password"
        self.submit = "#submit"
        self.error = "#error"

    def open(self):
        self.page.goto(self.url, wait_until="domcontentloaded", timeout=60000)

    def login(self, user, pwd):
        self.page.fill(self.username, user)
        self.page.fill(self.password, pwd)
        self.page.click(self.submit)

    def error_message(self):
        return self.page.text_content(self.error) or ""
