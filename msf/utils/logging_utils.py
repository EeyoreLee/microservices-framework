# -*- encoding: utf-8 -*-
'''
@create_time: 2022/11/21 11:05:27
@author: lichunyu
'''
import logging
from logging.config import dictConfig


_logconfig_dict_default = {
    "version": 1,
    "incremental": False,
    "disable_existing_loggers": False,
    "root": {
        "level": "INFO",
        "handlers": ["console"]
    },
    "formatters": {
        "default": {
            "class": "logging.Formatter",
            "format": "%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S %z"
        }
    },
    "handlers": {
        "timed_rotating_file_handler": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "default",
            "filename": "log.log",
            "when": "D",
            "backupCount": 7,
            "interval": 1,
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "stream": "ext://sys.stdout"
        },
    },
    "loggers": {
        "msf": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": True,
            "qualname": "msf"
        }
    }
}



def logger_setup(logconfig_dict):
    config = _logconfig_dict_default.copy()
    config.update(logconfig_dict)
    try:
        dictConfig(config)
    except (
            AttributeError,
            ImportError,
            ValueError,
            TypeError
    ) as exc:
        raise RuntimeError(str(exc))


dictConfig(_logconfig_dict_default)
logger = logging.getLogger("msf")