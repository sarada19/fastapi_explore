import os
import logging
import logging.config

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# General settings
DEBUG = True
ENV = "development"

LOG_FILE = os.path.join(BASE_DIR, 'app.log')

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': 'DEBUG' if DEBUG else 'INFO',
            'stream': 'ext://sys.stdout',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'level': 'DEBUG' if DEBUG else 'INFO',
            'filename': LOG_FILE,
            'maxBytes': 5 * 1024 * 1024,  # 5 MB
            'backupCount': 3,
            'encoding': 'utf8',
        },
    },

    'loggers': {
        '': {  # root logger
            'handlers': ['console', 'file'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': False,
        },
        # You can add more specific loggers here, e.g.:
        # 'app': {
        #     'handlers': ['console', 'file'],
        #     'level': 'DEBUG',
        #     'propagate': False,
        # },
    }
}

def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)


# If run as main script for testing
# if __name__ == "__main__":
#     setup_logging()
#     logger = logging.getLogger(__name__)
#     logger.debug("Debug log - logging configured using dictConfig")
#     logger.info("Info log - logging is ready")
