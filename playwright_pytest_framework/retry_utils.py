from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

# Default retry decorator for Playwright actions
playwright_retry = retry(
    stop=stop_after_attempt(3),
    wait=wait_fixed(2),
    retry=retry_if_exception_type(PlaywrightTimeoutError)
) 