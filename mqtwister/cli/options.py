# SPDX-FileCopyrightText: 2025 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

import sys
from mqtwister.cli import BANNER_WIDTH
from mqtwister.cli.messages import get_message as m
from mqtwister.cli.tables import make_table
from mqtwister.utils.logging import logger
from mqtwister.utils.network import (
    get_arp_table, get_interfaces, get_interface_mac, validate_mac_address
)


def ask_lmac(context: dict) -> None:
    """Set the local MAC address in the context."""

    # Ask the user for a MAC address
    mac_address: str = input(m('prompt_set_lmac')).strip()
    context['lmac'] = mac_address
    logger.info(m('info_set_lmac', mac_address))


def ask_ifname(context: dict) -> None:
    """Set the interface name in the context."""

    # Ask the user for an interface name
    interface_name: str = input(m('prompt_set_ifname')).strip()
    context['ifname'] = interface_name
    context['lmac'] = get_interface_mac(interface_name)
    logger.info(m('info_set_ifname', interface_name))
    if not context['lmac']:
        logger.warning(m('warning_mac_address_not_found', interface_name))


def show_ARP_table() -> None:
    """Display the ARP table."""

    # Retrieve the ARP table and order it by IP address
    logger.info(m('info_getting_arp_table'))
    arp_table: dict[str, str] = get_arp_table()
    logger.debug(m('debug_arp_table', arp_table))

    # Print the ARP table in a formatted way
    table: str = make_table(
        headers=[m('th_arp_table_ip'), m('th_arp_table_mac')],
        rows=[[ip, mac] for ip, mac in arp_table.items()],
    )
    print(table)

    # Warn if the ARP table is empty
    if not arp_table:
        logger.warning(m('warning_arp_table_empty'))


def show_interfaces() -> None:
    """Display the network interfaces."""

    # Retrieve network interfaces
    interfaces: list[str] = get_interfaces()

    # Retrieve MAC addresses for each interface
    mac_addresses: list[str] = [
        mac if (mac := get_interface_mac(i)) else 'N/A' for i in interfaces
    ]

    # Print the interfaces and their MAC addresses in a formatted way
    table: str = make_table(
        headers=[m('th_interface_mac'), m('th_interface_name')],
        rows=list(zip(mac_addresses, interfaces)),
    )
    print(table)


def show_config(context: dict) -> None:
    """Display the current configuration."""

    TABLE_WIDTH: int = BANNER_WIDTH

    # Print the current configuration in a formatted way
    table: str = '' \
        + f"{'=' * TABLE_WIDTH}\n" \
        + f"{m('th_config'):^{TABLE_WIDTH}}\n" \
        + f"{'-' * TABLE_WIDTH}\n" \
        + f"Interface Name: {context.get('ifname')}\n" \
        + f"Local MAC Address: {context.get('lmac')}\n" \
        + f"Target MAC Address: {context.get('TARGET_MAC_ADDRESS')}\n" \
        + f"{'=' * TABLE_WIDTH}\n"
    print(table, end='')


def check_config(context: dict) -> None:

    # Interface configuration
    if not (ifname := context.get('ifname')):
        logger.warning(m('warning_ifname_empty', ifname))
    elif ifname not in get_interfaces():
        logger.warning(m('warning_interface_not_found', ifname))

    # Local MAC address
    if not (lmac := context.get('lmac')):
        logger.warning(m('warning_lmac_empty', lmac))
    elif not validate_mac_address(lmac):
        logger.warning(m('warning_lmac_invalid', lmac))
    elif lmac != get_interface_mac(ifname):
        logger.warning(m('warning_lmac_mismatch', lmac, ifname))


def end_program() -> None:
    """End the program."""

    # Exit the program with a goodbye message :)
    print(m('menu_goodbye'))
    sys.exit(0)


def get_options(context: dict) -> dict[str, tuple[callable, str, bool]]:
    """Return the available options for the menu."""

    # {'key': (function, description, requires_context)}
    return {
        '1': (show_config, m('menu_op_show_config'), True),
        '2': (show_ARP_table, m('menu_op_show_arp_table'), False),
        '3': (show_interfaces, m('menu_op_show_interfaces'), False),
        '4': (ask_ifname, m('menu_op_set_ifname'), True),
        '5': (ask_lmac, m('menu_op_set_lmac'), True),
        'Q': (end_program, m('menu_op_goodbye'), False),
    }
