import os
import logging
import logging.config

import logstash

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
ENV = "development"

LOG_FILE = os.path.join(BASE_DIR, 'app.log')

class EnvFilter(logging.Filter):
    def __init__(self, env):
        super().__init__()
        self.env = env

    def filter(self, record):
        if DEBUG:
            return True
        return getattr(record, 'env', None) == self.env

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    'filters': {
        'env_filter': {
            '()': EnvFilter,
            'env': ENV,
        },
    },

    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'logstash': {
            '()': 'logstash.formatter.LogstashFormatter',
        }
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': 'DEBUG' if DEBUG else 'INFO',
            'stream': 'ext://sys.stdout',
            'filters': ['env_filter'],
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'level': 'DEBUG' if DEBUG else 'INFO',
            'filename': LOG_FILE,
            'maxBytes': 5 * 1024 * 1024,
            'backupCount': 3,
            'encoding': 'utf8',
            'filters': ['env_filter'],
        },
        'logstash': {
            'class': 'logstash.TCPLogstashHandler',
            'level': 'INFO',
            'host': 'your-logstash-host',  # e.g., 'localhost' or ELK server IP
            'port': 5000,                  # default Logstash TCP port or your configured port
            'version': 1,
            'formatter': 'logstash',
        },
    },

    'loggers': {
        '': {
            'handlers': ['console', 'file', 'logstash'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': False,
        },
    }
}

def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)