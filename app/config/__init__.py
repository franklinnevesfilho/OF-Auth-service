from . import database
from .scheduler import scheduler

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s:%(asctime)s\t-\t%(message)s'
)

logger = logging.getLogger(__name__)
