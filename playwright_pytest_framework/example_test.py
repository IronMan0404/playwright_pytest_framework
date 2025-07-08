import pytest
from .actions import click_with_retry
from .utils import wait_for_element
from .login_utils import login


def test_example(page):
    page.goto("https://playwright.dev/")
    wait_for_element(page, "text=Get Started")
    click_with_retry(page, "text=Get Started")
    wait_for_element(page, "h1")
    assert "Playwright" in page.title() 


def test_login(page):
    login(page, "https://example.com/login", "myuser", "mypassword")
    # Add assertions or further steps as needed 