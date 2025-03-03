import logging
from ..config import LOGGING_LEVEL

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=LOGGING_LEVEL,
    format='[%(levelname)s] %(message)s'
)
