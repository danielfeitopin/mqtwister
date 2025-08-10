# SPDX-FileCopyrightText: 2025 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

from mqtwister.cli import BANNER_WIDTH
from mqtwister.cli.messages import get_message as m
from mqtwister.cli.tables import DELIMITER, HEADER_SEPARATOR
from mqtwister.cli.options import get_options, check_config
from mqtwister.utils.logging import logger


def show_menu(context: dict) -> None:
    """Display the main menu."""

    TABLE_WIDTH: int = BANNER_WIDTH

    # Get available options
    options: dict[str, tuple[callable, str, bool]] = get_options()

    # Display menu options in a formatted way
    table: str = '' \
        + f"{DELIMITER * TABLE_WIDTH}\n" \
        + f"{m('th_menu').center(TABLE_WIDTH)}\n" \
        + f"{HEADER_SEPARATOR * TABLE_WIDTH}\n" \
        + f"{'\n'.join(f"[{k}] {v[1]}" for k, v in options.items())}\n" \
        + f"{DELIMITER * TABLE_WIDTH}"
    print(table)

    # Check configuration before proceeding
    check_config(context)

    # Prompt for user input
    choice: str = input(m('menu_prompt')).upper().strip()
    print()

    # Execute the chosen option or show an error message
    if choice in options and options[choice][2]:  # Requires context
        try:
            options[choice][0](context)
        except KeyboardInterrupt:
            logger.info(m('info_operation_cancelled'))
    elif choice in options:  # Does not require context
        try:
            options[choice][0]()
        except KeyboardInterrupt:
            logger.info(m('info_operation_cancelled'))
    else:  # Invalid choice
        print(m('menu_invalid_choice'))
        
    
