# SPDX-FileCopyrightText: 2025 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL

# Debugging
LOGGING_LEVEL: int | None = DEBUG

# Host configuration
INTERFACE_NAME: str = ''

# Target configuration
TARGET_IP: str = ''
MQTT_PORT: int = 1883
