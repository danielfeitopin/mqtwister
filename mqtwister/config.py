# SPDX-FileCopyrightText: 2025 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL

# Language configuration
DEFAULT_LANGUAGE: str = 'en'
SUPPORTED_LANGUAGES: set[str] = {'en', 'es', 'gl'}

# Debugging
LOGGING_LEVEL: int | None = DEBUG

# Host configuration
INTERFACE_NAME: str = 'Wi-Fi'

# Target configuration
MQTT_PORT: int = 1883
