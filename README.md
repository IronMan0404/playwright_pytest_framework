# Playwright Pytest Framework

A robust, reusable Playwright + pytest framework with utilities, actions, retries, loggers, and better timeouts. Designed to be used as a package for easy import and extension by consumers.

## Features
- Playwright browser automation with pytest
- Custom actions and utilities
- Robust retry logic (via tenacity)
- Advanced logging (via loguru)
- Configurable timeouts
- Helper bot for scaffolding utilities
- Semi-automated codegen-to-framework refactoring

## Installation

```bash
python -m venv venv
venv\Scripts\pip install --upgrade pip setuptools wheel
venv\Scripts\pip install -r requirements.txt
pip install .
```

## Usage

### 1. Record Flows with Playwright Codegen

Use Playwright's codegen tool to record your browser interactions:

```bash
venv\Scripts\playwright codegen https://your-app-url.com
```
- Interact with your app in the opened browser.
- Copy the generated Python code and save it to a file (e.g., `raw_code.py`).

### 2. Refactor Codegen Output to Use Framework Methods

Use the provided `refactor_codegen.py` script to automatically replace raw Playwright calls with your framework's robust utilities:

```bash
venv\Scripts\python refactor_codegen.py raw_code.py
```
- This will create `raw_code_refactored.py` with:
  - `page.click(...)` replaced by `click_with_retry(page, ...)`
  - `page.wait_for_selector(...)` replaced by `wait_for_element(page, ...)`
  - Necessary imports added

### 3. Integrate and Extend

- Copy the refactored code into your test or utility files.
- Further tweak as needed (e.g., add waits before fills, assertions, etc.).
- Use your helper bot to scaffold new utilities:

```bash
venv\Scripts\python helper_bot.py
```
- Follow the prompts to generate login, home page, or other utilities.

### 4. Run Your Tests

```bash
venv\Scripts\pytest
```

## Example: Refactored Login Flow

```python
from playwright_pytest_framework.utils import wait_for_element
from playwright_pytest_framework.actions import click_with_retry

def test_login(page):
    page.goto("https://example.com/login")
    wait_for_element(page, "input[name='username']")
    page.fill("input[name='username']", "myuser")
    wait_for_element(page, "input[name='password']")
    page.fill("input[name='password']", "mypassword")
    click_with_retry(page, "button[type='submit']")
    wait_for_element(page, "#dashboard")
```

## Development

- Install dependencies: `pip install -e .`
- Run tests: `pytest`
- Scaffold utilities: `python helper_bot.py`
- Refactor codegen output: `python refactor_codegen.py <input_file.py>`

---

**This workflow lets you record, refactor, and robustly automate browser flows with minimal manual effort!** 