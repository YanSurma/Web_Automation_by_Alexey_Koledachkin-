import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        page.set_default_timeout(30000)
        yield page
        page.close()
        context.close()
        browser.close()
