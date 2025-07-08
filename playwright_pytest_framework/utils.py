from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type
from loguru import logger

@retry(stop=stop_after_attempt(5), wait=wait_fixed(1), retry=retry_if_exception_type(PlaywrightTimeoutError))
def wait_for_element(page: Page, selector: str, timeout: int = 5000):
    logger.info(f"Waiting for selector: {selector} with timeout {timeout}ms")
    try:
        page.wait_for_selector(selector, timeout=timeout)
        logger.success(f"Element appeared: {selector}")
    except PlaywrightTimeoutError as e:
        logger.error(f"Timeout while waiting for selector: {selector}")
        raise 