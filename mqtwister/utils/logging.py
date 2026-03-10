# SPDX-FileCopyrightText: 2026 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

import logging
from ..config import LOGGING_LEVEL

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=LOGGING_LEVEL,
    format='[%(levelname)s] %(message)s'
)
