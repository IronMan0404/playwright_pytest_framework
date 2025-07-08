from loguru import logger
import sys

def setup_logging():
    logger.remove()
    logger.add(sys.stdout, level="INFO", format="[{time:YYYY-MM-DD HH:mm:ss}] [{level}] {message}")
    logger.add("framework.log", rotation="1 MB", retention="10 days", level="DEBUG")

# Call setup_logging on import for convenience
setup_logging() 