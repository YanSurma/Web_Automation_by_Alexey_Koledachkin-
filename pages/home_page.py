from pages.base_page import BasePage


class HomePage(BasePage):
    _PAGE_URL = 'https://demo.opensource-socialnetwork.org/home'
    _CREATE_POST_INPUT = '//textarea[@name="post"]'
    _CREATE_POST_BUTTON = '//input[@value="Post"]'
    _FIRST_POST_TEXT_CONTENT = '(//div[@class="post-contents"]/p)[1]'

    def create_post(self):
        post_text = self.fake.text(20)
        self.fill_input(self._CREATE_POST_INPUT, post_text)
        self.click(self._CREATE_POST_BUTTON)
        self.page.reload()
        return post_text

    def is_post_published(self, post_text_value):
        self.find(f"p:text('{post_text_value}')").wait_for()
