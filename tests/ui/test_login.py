import pytest
from pages.login_page import LoginPage
from utils.test_data import INVALID_CREDENTIALS, VALID_PASSWORD, VALID_USER


@pytest.mark.ui
class TestLogin:
    def test_login_success(self, login_page: LoginPage):
        login_page.open().login(VALID_USER, VALID_PASSWORD)
        assert "/inventory.html" in login_page.page.url

    @pytest.mark.parametrize("username,password", INVALID_CREDENTIALS)
    def test_invalid_login(self, login_page: LoginPage, username, password):
        login_page.open().login(username, password)
        assert login_page.has_error()