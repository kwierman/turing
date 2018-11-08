import logging

DEBUG=True

try:
    from .local import *
except ImportError:
    logging.warning("No local settings defined. Using Defaults")
