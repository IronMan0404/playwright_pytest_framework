from playwright.sync_api import Page
from playwright_pytest_framework.utils import wait_for_element
from playwright_pytest_framework.actions import click_with_retry
from playwright_pytest_framework.timeouts import DEFAULT_ACTION_TIMEOUT
from playwright_pytest_framework.logging_config import logger

def go_to_home(page: Page, base_url: str):
    logger.info(f"Navigating to home page: {base_url}")
    page.pause()  # Open Playwright debugger
    page.goto(base_url)
    wait_for_element(page, "#home-banner", timeout=DEFAULT_ACTION_TIMEOUT)
    logger.success("Home page loaded!")
