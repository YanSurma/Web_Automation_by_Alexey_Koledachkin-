import allure

from tests.base_test import BaseTest


@allure.epic("Users")
@allure.feature("Accounts")
@allure.story("Create accounts")
class TestRegistrationPage(BaseTest):

    @allure.title("Create account")
    def test_create_account(self):
        self.registration_page.open()
        self.registration_page.create_account()
        self.registration_page.is_account_created()
