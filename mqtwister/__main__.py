# SPDX-FileCopyrightText: 2025 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

import sys


def import_modules() -> None:
    """Import all necessary modules to ensure they are available when needed."""

    # Retrieve and set language from config
    print('Loading language module...', end=' ')
    from .config import DEFAULT_LANGUAGE
    from mqtwister.lang import LanguageManager, get_message as m
    LanguageManager.set_language(DEFAULT_LANGUAGE)
    print(f"\r\033[2K{m('init_set_language', DEFAULT_LANGUAGE)}", end=' ')

    # Import UI components
    print(f"\r\033[2K{m('init_load_ui')}", end=' ')
    import mqtwister.ui.banner
    import mqtwister.ui.menu
    import mqtwister.ui.options
    import mqtwister.ui.tables

    # Import utilities
    print(f"\r\033[2K{m('init_load_utils')}", end=' ')
    import mqtwister.utils.logging
    import mqtwister.utils.network

    # Import processing components
    print(f"\r\033[2K{m('init_load_processing')}", end=' ')
    import mqtwister.processor
    import mqtwister.processor.sniffer

    # Clear the line after loading is complete
    print(end="\r\033[2K")


def get_context() -> dict:
    """Initialize and return the context dictionary with default values."""

    from mqtwister.config import MQTT_PORT

    return {
        'credentials': set(),  # Set of detected credentials {(id, user, pwd),}
        'ifname': None,  # Interface name
        'lmac': None,    # Local MAC address
        'lport': MQTT_PORT,  # Listening port
        'rules': [],      # List of rules
        'sniffer': None,  # Sniffer instance
        'sniffer_running': False,  # Flag to check if sniffer is running
        'show_menu': True,  # Flag to show the menu
    }


def main(context: dict = {}) -> None:
    """Main function to run MQTwister."""

    # Display banner
    from mqtwister.ui.banner import Banner
    print(Banner.get_colorful_banner(Banner.DEFAULT_COLOR))

    # Show the main menu
    from mqtwister.ui.menu import show_menu
    while context.get('show_menu', True):
        show_menu(context)
        print()


if __name__ == "__main__":

    import_modules()

    from mqtwister.lang import get_message as m
    from mqtwister.utils.logging import logger

    try:
        main(context=get_context())

    except KeyboardInterrupt:
        sys.exit(0)

    except PermissionError:
        logger.error(m('error_permission_denied'))
        sys.exit(1)
