import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage

import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные из .env

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.page = page
        self.login_page = LoginPage(page)
        self.home_page = HomePage(page)
        self.registration_page = RegistrationPage(page)
