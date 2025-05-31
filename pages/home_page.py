import allure

from data.links import Links
from pages.base_page import BasePage


class HomePage(BasePage):
    _PAGE_URL = Links.HOME_PAGE
    _CREATE_POST_INPUT = '//textarea[@name="post"]'
    _CREATE_POST_BUTTON = '//input[@value="Post"]'
    _FIRST_POST_TEXT_CONTENT = '(//div[@class="post-contents"]/p)[1]'

    def create_post(self):
        with allure.step("Create post"):
            self.post_text = self.fake.text(20)
            self.fill_input(self._CREATE_POST_INPUT, self.post_text)
            self.click(self._CREATE_POST_BUTTON)
            self.page.reload()

    def is_post_created(self):
        with allure.step("Check that post is published"):
            self.find(f"p:text('{self.post_text}')").wait_for()
