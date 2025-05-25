import allure

from tests.base_test import BaseTest, USERNAME, PASSWORD


@allure.epic("Home page")
@allure.feature("Create posts")
@allure.story("Create new post")
class TestHomePage(BaseTest):

    @allure.title("Login and create post")
    def test_login_and_post(self):
        self.login_page.open()
        self.login_page.login_as(USERNAME, PASSWORD)
        self.home_page.open()
        self.home_page.create_post()
        self.home_page.is_post_created()

    @allure.title("Login with declarative method")
    def test_successful_login_declarative(self):
        self.login_page.open()
        self.login_page.login_as(USERNAME, PASSWORD)

    @allure.title("Login with imperative method")
    def test_successful_login_imperative(self):
        self.login_page.open()
        self.login_page.fill_username_input(USERNAME)
        self.login_page.fill_password_input(PASSWORD)
        self.login_page.click_login_button()
