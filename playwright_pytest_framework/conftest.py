import pytest
from playwright.sync_api import sync_playwright
from .logging_config import setup_logging

@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    setup_logging()

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()