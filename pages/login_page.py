from playwright.sync_api import Page
from utils.test_data import BASE_URL


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_btn = page.locator("#login-button")
        self.error_alert = page.locator("[data-test='error']")

    def open(self):
        self.page.goto(BASE_URL)
        return self

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_btn.click()

    def has_error(self) -> bool:
        return self.error_alert.is_visible()

    def get_error_message(self) -> str:
        return self.error_alert.text_content().strip()