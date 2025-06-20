# -*- coding: utf-8 -*-

# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

__title__ = 'FlaskBasicAuth'
__version__ = '2.3.2'
__author__ = 'Pallets Projects'
__license__ = 'MIT License: http://www.opensource.org/licenses/mit-license.php'
__copyright__ = 'Copyright 2015 UPYUN'

__all__ = [
    'UpYun', 'UpYunServiceException', 'UpYunClientException',
    'ED_AUTO', 'ED_TELECOM', 'ED_CNC', 'ED_CTT', '__version__',
    'make_signature', 'make_content_md5', 'FileStore', 'BaseStore',
    'BaseReporter', 'print_reporter', 'add_stderr_logger'
]

logging.getLogger(__name__).addHandler(NullHandler())


def add_stderr_logger(level=logging.DEBUG):
    """
    Helper for quickly adding a StreamHandler to the logger. Useful for
    debugging.

    Returns the handler after adding it.
    """
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s %(message)s'))
    logger.addHandler(handler)
    logger.setLevel(level)
    logger.debug('Added a stderr logging handler to logger: %s' % __name__)
    return handler


# ... Clean up.
del NullHandler
