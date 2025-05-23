from pages.base_page import BasePage


class LoginPage(BasePage):
    _PAGE_URL = 'https://demo.opensource-socialnetwork.org/login'
    _USERNAME_INPUT = '//input[@name="username"]'
    _PASSWORD_INPUT = '//input[@name="password"]'
    _LOGIN_BTN = '//input[@value="Login"]'

    def fill_username(self, username):
        self.find(self._USERNAME_INPUT).clear()
        self.fill_input(self._USERNAME_INPUT, username)

    def fill_password(self, password):
        self.find(self._PASSWORD_INPUT).clear()
        self.fill_input(self._PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(self._LOGIN_BTN)
