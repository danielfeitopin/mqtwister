# SPDX-FileCopyrightText: 2025 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

import sys
from mqtwister.cli import BANNER_WIDTH
from mqtwister.lang import get_message as m
from mqtwister.cli.tables import make_table
from mqtwister.utils.logging import logger
from mqtwister.utils.network import (
    get_arp_table, get_interfaces, get_interface_mac, validate_mac_address
)


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
        + f"Listening Port: {context.get('lport')}\n" \
        + f"Target MAC Address: {context.get('TARGET_MAC_ADDRESS')}\n" \
        + f"Sniffer running: {'Yes' if context.get('sniffer') else 'No'}\n" \
        + f"{'=' * TABLE_WIDTH}\n"
    print(table, end='')


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


def ask_ifname(context: dict) -> None:
    """Set the interface name in the context."""

    # Ask the user for an interface name
    interface_name: str = input(m('prompt_set_ifname')).strip()
    context['ifname'] = interface_name
    context['lmac'] = get_interface_mac(interface_name)
    logger.info(m('info_set_ifname', interface_name))
    if not context['lmac']:
        logger.warning(m('warning_mac_address_not_found', interface_name))


def ask_lmac(context: dict) -> None:
    """Set the local MAC address in the context."""

    # Ask the user for a MAC address
    mac_address: str = input(m('prompt_set_lmac')).strip()
    context['lmac'] = mac_address
    logger.info(m('info_set_lmac', mac_address))


def ask_port(context: dict) -> None:
    """Set the MQTT port in the context."""

    # Ask the user for a port number
    try:
        port: int = int(input(m('prompt_set_port')).strip())
        if port <= 0 or port > 65535:
            raise ValueError
        context['lport'] = port
    except ValueError:
        logger.error(m('error_invalid_port'))


def show_rules(context: dict) -> None:
    """Display the current rules."""

    # Print the rules in a formatted way
    table: str = make_table(
        headers=[
            '#'.center(3),
            m('th_rule_topic'),
            m('th_rule_payload'),
            m('th_rule_topic_op_name'),
            m('th_rule_topic_op_args'),
            m('th_rule_payload_op_name'),
            m('th_rule_payload_op_args'),
        ],
        rows=[
            [i, repr(rule.topic), repr(rule.payload), rule.topic_op[0],
                repr(rule.topic_op[1]), rule.payload_op[0], repr(rule.payload_op[1])]
            for i, rule in enumerate(context['rules'])],
    )
    print(table)


def add_rule(context: dict) -> None:
    """Add a new rule to the context."""

    from mqtwister.processor.rules import Rule

    rule_str: str = input(m('prompt_add_rule')).strip()

    try:
        rule: Rule = Rule.from_str(rule_str)
        if rule.is_empty():
            logger.warning(m('warning_empty_rule'))
        elif rule in context['rules']:
            logger.warning(m('warning_existing_rule'))
        else:
            context['rules'].append(rule)
            logger.info(m('info_rule_added', rule))
    except ValueError as e:
        logger.error(m('error_invalid_rule', e))


def del_rule(context: dict) -> None:
    """Delete a rule from the context."""

    if not context['rules']:
        logger.warning(m('warning_no_rules'))
        return

    try:
        i: int = int(input(m('prompt_del_rule')).strip())
        rule = context['rules'].pop(i)
        logger.info(m('info_rule_deleted', rule))
    except (ValueError, IndexError):
        logger.error(m('error_invalid_rule_number'))
        return


def start_mitm(context: dict) -> None:
    """Start the MitM with the current context."""

    # Start the sniffer
    from mqtwister.processor.sniffer import get_sniffer
    from mqtwister.processor.mqtt import packet_callback as prn

    # Ensure sniffer is initialized in the context
    if not context.get('sniffer'):
        context['sniffer'] = get_sniffer(context, prn)

    # Start the sniffer and handle exceptions
    try:
        print("Press ENTER to stop the sniffer...\n")
        context['sniffer'].start()

        if context['sniffer'].exception:
            raise context['sniffer'].exception

        context['sniffer_running'] = context['sniffer'].running

        input()
        if context['sniffer'].running:
            context['sniffer'].stop()
        context['sniffer_running'] = context['sniffer'].running
        context['sniffer'] = None  # Clear sniffer instance

    except Exception as e:
        logger.error(e)
        sys.exit(-1)
    except KeyboardInterrupt:
        sys.exit(0)


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
    elif ifname and lmac != get_interface_mac(ifname):
        logger.warning(m('warning_lmac_mismatch', lmac, ifname))


def end_program() -> None:
    """End the program."""

    # Exit the program with a goodbye message :)
    print(m('menu_goodbye'))
    sys.exit(0)


def get_options() -> dict[str, tuple[callable, str, bool]]:
    """Return the available options for the menu."""

    # {'key': (function, description, requires_context)}
    return {
        '1': (show_config, m('menu_op_show_config'), True),
        '2': (show_ARP_table, m('menu_op_show_arp_table'), False),
        '3': (show_interfaces, m('menu_op_show_interfaces'), False),
        '4': (ask_ifname, m('menu_op_set_ifname'), True),
        '5': (ask_lmac, m('menu_op_set_lmac'), True),
        '6': (ask_port, m('menu_op_set_port'), True),
        '7': (show_rules, m('menu_op_show_rules'), True),
        '8': (add_rule, m('menu_op_add_rule'), True),
        '9': (del_rule, m('menu_op_del_rule'), True),
        '0': (start_mitm, m('menu_op_start_mitm'), True),
        'Q': (end_program, m('menu_op_goodbye'), False),
    }
