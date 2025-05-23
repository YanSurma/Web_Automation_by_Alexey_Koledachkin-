from faker import Faker
from playwright.sync_api import Page, expect


class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.fake = Faker()

    def open(self):
        self.page.goto(self._PAGE_URL)

    def is_open(self, path_of_url):
        assert path_of_url in self.page.url, f"URL does not contain '{path_of_url}', the page did not open."
        return True

    def find(self, locator):
        return self.page.locator(locator)

    def find_all(self, locator):
        return self.page.query_selector_all(locator)

    def click(self, locator):
        self.find(locator).click()

    def fill_input(self, locator, text):
        self.click(locator)
        self.page.keyboard.type(text)

    def fill_keyboard(self, locator, text):
        self.click(locator)
        self.page.keyboard.type(text)

    def is_element_contain_text(self, locator, text):
        element = self.find(locator)
        expect(element).to_contain_text(text)

    def is_element_visible(self, locator, timeout=5000):
        try:
            self.page.wait_for_selector(locator, timeout=timeout)
            return True
        except Exception:
            return False
