# SPDX-FileCopyrightText: 2025 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

MESSAGES: dict[str, str] = {  # Could be replaced by a localization system

    # Menu entries, prompts, and actions
    'menu_prompt': "Enter your choice: ",
    'menu_invalid_choice': "Invalid choice, please try again.",
    'th_menu': "MAIN MENU",
    'info_operation_cancelled': "Operation cancelled by user.",

    'menu_op_goodbye': "Exit.",
    'menu_goodbye': "Goodbye!",

    'menu_op_show_config': "Show Current Configuration.",
    'th_config': "Current Configuration",
    'warning_ifname_empty': "Interface name is empty.",
    'warning_lmac_empty': "Local MAC address is empty.",
    'warning_lmac_invalid': "Invalid MAC address: {}.",
    'warning_lmac_mismatch': "Local MAC address {} does not match the interface MAC address for {}.",

    'menu_op_show_arp_table': "Show ARP Table.",
    'th_arp_table_ip': "IP Address",
    'th_arp_table_mac': "MAC Address",

    'menu_op_show_interfaces': "Show Interfaces.",
    'th_interface_mac': "MAC Address",
    'th_interface_name': "Interface Name",

    'menu_op_set_lmac': "Set Local MAC Address.",
    'prompt_set_lmac': "Enter the local MAC address: ",
    'info_set_lmac': "MAC address set to {}.",

    'menu_op_set_ifname': "Set Interface Name.",
    'prompt_set_ifname': "Enter the interface name: ",
    'info_set_ifname': "Interface name set to {}.",

    # Network notifications
    'info_getting_arp_table': "Getting ARP table...",
    'debug_arp_table': "ARP table: {}",
    'warning_arp_table_empty': "ARP table is empty or could not be retrieved.",
    'warning_interface_not_found': "Interface '{}' not found.",
    'warning_mac_address_not_found': "MAC address not found for interface '{}'",

    'error_permission_denied': "Permission denied. Please run as administrator.",
}


def get_message(key: str, *args) -> str:
    """Retrieve a message by key and format it with the provided arguments."""
    # return MESSAGES.get(key, '').format(*args)
    return MESSAGES[key].format(*args)
