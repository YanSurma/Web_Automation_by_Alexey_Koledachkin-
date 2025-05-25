import allure

from pages.base_page import BasePage


class LoginPage(BasePage):
    _PAGE_URL = 'https://demo.opensource-socialnetwork.org/login'
    _USERNAME_INPUT = '//input[@name="username"]'
    _PASSWORD_INPUT = '//input[@name="password"]'
    _LOGIN_BTN = '//input[@value="Login"]'

    def fill_username_input(self, username):
        with allure.step(f"Fill text: {username} to input: {self._USERNAME_INPUT}"):
            self.find(self._USERNAME_INPUT).clear()
            self.fill_input(self._USERNAME_INPUT, username)

    def fill_password_input(self, password):
        with allure.step(f"Fill text: {password} to input: {self._PASSWORD_INPUT}"):
            self.find(self._PASSWORD_INPUT).clear()
            self.fill_input(self._PASSWORD_INPUT, password)

    def click_login_button(self):
        with allure.step(f"CLick login button"):
            self.click(self._LOGIN_BTN)

    def login_as(self, username, password):
        with allure.step(f"Login with username: {username} and password: {password}"):
            self.fill_username_input(username)
            self.fill_password_input(password)
            self.click_login_button()
