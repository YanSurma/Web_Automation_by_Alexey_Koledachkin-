from tests.base_test import BaseTest


class TestHomePage(BaseTest):

    def test_login_and_post(self):
        self.login_page.open()
        self.login_page.fill_username('administrator')
        self.login_page.fill_password('administrator')
        self.login_page.click_login_button()
        self.home_page.open()
        new_post = self.home_page.create_post()
        self.home_page.is_post_published(new_post)
