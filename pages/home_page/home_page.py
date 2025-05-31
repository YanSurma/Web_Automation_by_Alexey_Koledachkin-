from data.links import Links
from pages.base_page import BasePage
from pages.home_page.components.post_block import PostBlock


class HomePage(BasePage):
    _PAGE_URL = Links.HOME_PAGE

    def __init__(self, page):
        super().__init__(page)
        self.post_block = PostBlock(page)
