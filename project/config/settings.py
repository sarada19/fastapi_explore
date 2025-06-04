import os
import logging
import logging.config
import logging.handlers
from dotenv import load_dotenv

# Load env vars
ENV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env.staging')
load_dotenv(dotenv_path=ENV_PATH)

DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
ENV = os.getenv('ENV', 'development')
LOG_FILE = os.getenv('LOG_FILE', 'app.log')
LOGSTASH_HOST = os.getenv('LOGSTASH_HOST', 'localhost')
LOGSTASH_PORT = int(os.getenv('LOGSTASH_PORT', 5000))
LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG' if DEBUG else 'INFO').upper()


# Custom Filter
class EnvFilter(logging.Filter):
    def __init__(self, env):
        super().__init__()
        self.env = env

    def filter(self, record):
        # Pass all logs if DEBUG is on, else only logs matching environment
        if DEBUG:
            return True
        return getattr(record, 'env', None) == self.env


# Custom JSON TCP Handler
class JSONTcpHandler(logging.handlers.SocketHandler):
    def makePickle(self, record):
        formatted = self.format(record)
        if isinstance(formatted, str):
            formatted = formatted.encode('utf-8')
        return formatted + b'\n'

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
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
        'json': {
            'format': '{"timestamp": "%(asctime)s", "level": "%(levelname)s", "name": "%(name)s", "message": "%(message)s"}'
        },
        'logstash': {
            '()': 'logstash_formatter.LogstashFormatter',
        },
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': LOG_LEVEL,
            'filters': ['env_filter'],
            'stream': 'ext://sys.stdout',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'level': LOG_LEVEL,
            'filename': LOG_FILE,
            'maxBytes': 5 * 1024 * 1024,
            'backupCount': 3,
            'encoding': 'utf8',
            'filters': ['env_filter'],
        },
        'logstash': {
            'class': 'logging.handlers.SocketHandler',
            'level': LOG_LEVEL,
            'host': LOGSTASH_HOST,
            'port': LOGSTASH_PORT,
            'formatter': 'logstash',
            'filters': ['env_filter'],
        },
        'json_tcp': {
            '()': JSONTcpHandler,
            'level': LOG_LEVEL,
            'host': LOGSTASH_HOST,
            'port': LOGSTASH_PORT,
            'formatter': 'json',
            'filters': ['env_filter'],
        },
    },

    'loggers': {
        'fastapi_logger': {
            'handlers': ['console', 'file', 'logstash', 'json_tcp'],
            'level': LOG_LEVEL,
            'propagate': False,
        },
        'uvicorn.error': {
            'handlers': ['console', 'file', 'logstash'],
            'level': LOG_LEVEL,
            'propagate': False,
        },
        'uvicorn.access': {
            'handlers': ['console', 'file', 'logstash'],
            'level': LOG_LEVEL,
            'propagate': False,
        },
    },

    'root': {
        'handlers': ['console', 'file', 'logstash', 'json_tcp'],
        'level': LOG_LEVEL,
    },
}

def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)