import os
from pathlib import Path

LOGIN_TEMPLATE = '''from playwright.sync_api import Page
from playwright_pytest_framework.utils import wait_for_element
from playwright_pytest_framework.actions import click_with_retry
from playwright_pytest_framework.timeouts import DEFAULT_ACTION_TIMEOUT
from playwright_pytest_framework.logging_config import logger

def login(page: Page, base_url: str, username: str, password: str):
    logger.info(f"Navigating to {base_url}")
    page.pause()  # Open Playwright debugger
    page.goto(base_url)
    wait_for_element(page, "input[name='username']", timeout=DEFAULT_ACTION_TIMEOUT)
    page.fill("input[name='username']", username)
    wait_for_element(page, "input[name='password']", timeout=DEFAULT_ACTION_TIMEOUT)
    page.fill("input[name='password']", password)
    click_with_retry(page, "button[type='submit']", timeout=DEFAULT_ACTION_TIMEOUT)
    wait_for_element(page, "#dashboard", timeout=DEFAULT_ACTION_TIMEOUT)
    logger.success("Login successful!")
'''

HOME_PAGE_TEMPLATE = '''from playwright.sync_api import Page
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
'''

def main():
    print("Welcome to the Playwright Pytest Framework Helper Bot!")
    action = input("What utility do you want to create? (e.g., login, home_page): ").strip().lower()
    if action == "login":
        utils_path = Path("playwright_pytest_framework/login_utils.py")
        template = LOGIN_TEMPLATE
    elif action == "home_page":
        utils_path = Path("playwright_pytest_framework/home_page_utils.py")
        template = HOME_PAGE_TEMPLATE
    else:
        print("Sorry, only 'login' and 'home_page' utilities are supported in this version.")
        return
    if utils_path.exists():
        print(f"{utils_path} already exists. Overwrite? (y/n): ", end="")
        if input().strip().lower() != 'y':
            print("Aborted.")
            return
    with open(utils_path, "w") as f:
        f.write(template)
    print(f"{action.replace('_', ' ').capitalize()} utility created at {utils_path}")

if __name__ == "__main__":
    main() 