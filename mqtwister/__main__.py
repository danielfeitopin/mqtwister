# SPDX-FileCopyrightText: 2025 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

def main(context: dict = {}) -> None:
    """Main function to run the MQTwister CLI."""

    # Display banner
    from .cli.banner import Banner
    print(Banner.get_colorful_banner(Banner.DEFAULT_COLOR))

    # Show the main menu
    from .cli.menu import show_menu
    while context.get('show_menu', True):
        show_menu(context)
        print()


if __name__ == "__main__":

    import sys
    from mqtwister.config import MQTT_PORT, DEFAULT_LANGUAGE

    from mqtwister.lang import LanguageManager, get_message as m
    LanguageManager.set_language(DEFAULT_LANGUAGE)

    from mqtwister.utils.logging import logger

    # Initialize context with default values
    context: dict = {
        # Set of detected credentials {(id, user, pwd)...}
        'credentials': set(),
        'ifname': None,  # Interface name
        'lmac': None,    # Local MAC address
        'lport': MQTT_PORT,  # Listening port
        'rules': [],      # List of rules
        'sniffer': None,  # Sniffer instance
        'sniffer_running': False,  # Flag to check if sniffer is running
        'show_menu': True,  # Flag to show the menu
    }

    try:
        main(context)

    except KeyboardInterrupt:
        sys.exit(0)

    except PermissionError:
        logger.error(m('error_permission_denied'))
        sys.exit(1)
