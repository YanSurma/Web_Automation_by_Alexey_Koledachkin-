import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.page = page
        self.login_page = LoginPage(page)
        self.home_page = HomePage(page)
        self.registration_page = RegistrationPage(page)
