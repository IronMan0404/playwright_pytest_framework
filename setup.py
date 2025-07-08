from setuptools import setup, find_packages

setup(
    name="playwright_pytest_framework",
    version="0.1.0",
    description="A robust pytest + Playwright framework with utilities, actions, retries, loggers, and better timeouts.",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "pytest",
        "playwright",
        "pytest-playwright",
        "loguru",
        "tenacity"
    ],
    python_requires=">=3.7",
) 