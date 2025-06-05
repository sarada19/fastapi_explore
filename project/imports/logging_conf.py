from project.config.settings import setup_logging
setup_logging()

import logging  # noqa: E402
logger = logging.getLogger("fastapi_logger")