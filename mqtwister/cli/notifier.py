# SPDX-FileCopyrightText: 2025 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

from mqtwister.cli.messages import get_message


class Notifier:
    """A simple notifier class to manage notifications in the CLI."""

    NOTIFICATIONS_ON: bool = True

    @classmethod
    def notify(cls, key, *args, force=False):
        """Prints a message if notifications are not paused."""
        if cls.NOTIFICATIONS_ON or force:
            print(get_message(key, *args))

    @classmethod
    def enable_notifications(cls) -> None:
        """Enable notifications."""
        cls.NOTIFICATIONS_ON = True

    @classmethod
    def disable_notifications(cls) -> None:
        """Disable notifications."""
        cls.NOTIFICATIONS_ON = False
