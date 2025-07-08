from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type
from loguru import logger

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2), retry=retry_if_exception_type(PlaywrightTimeoutError))
def click_with_retry(page: Page, selector: str, timeout: int = 5000):
    logger.info(f"Attempting to click selector: {selector} with timeout {timeout}ms")
    try:
        page.click(selector, timeout=timeout)
        logger.success(f"Clicked selector: {selector}")
    except PlaywrightTimeoutError as e:
        logger.error(f"Timeout while clicking selector: {selector}")
        raise 