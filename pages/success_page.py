class SuccessPage:
    def __init__(self, page):
        self.page = page
        self.heading = "text=Logged In Successfully"
        self.logout_link = "text=Log out"

    def wait_loaded(self):
        self.page.wait_for_selector(self.heading, timeout=60000)

    def is_loaded(self):
        return self.page.is_visible(self.heading)

    def logout(self):
        self.page.click(self.logout_link)
