# SPDX-FileCopyrightText: 2025 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

MESSAGES: dict[str, str] = {}

# Menu entries, prompts, and actions
MESSAGES.update({

    # Main menu
    'menu_prompt': "Enter your choice: ",
    'menu_invalid_choice': "Invalid choice, please try again.",
    'th_menu': "MAIN MENU",

    # Options - Show ARP table
    'menu_op_show_arp_table': "Show ARP Table.",
    'th_arp_table_ip': "IP Address",
    'th_arp_table_mac': "MAC Address",

    # Options - Show interfaces
    'menu_op_show_interfaces': "Show Interfaces.",
    'th_interface_mac': "MAC Address",
    'th_interface_name': "Interface Name",

    # Options - Set MAC address
    'menu_op_set_lmac': "Set Local MAC Address.",
    'prompt_set_lmac': "Enter the local MAC address: ",
    'info_set_lmac': "MAC address set to '{}'.",

    # Options - Set interface name
    'menu_op_set_ifname': "Set Interface Name.",
    'prompt_set_ifname': "Enter the interface name: ",
    'info_set_ifname': "Interface name set to '{}'.",

    # Options - Set listening port
    'menu_op_set_port': "Set Listening Port.",
    'prompt_set_port': "Enter the port to sniff (default 1883): ",
    'info_set_port': "Listening port set to '{}'.",
    'error_invalid_port': "Invalid port number. Please enter a valid port between 1 and 65535.",

    # Options - Show rules
    'menu_op_show_rules': "Show Rules.",
    'th_rule_topic': "Rule Topic",
    'th_rule_payload': "Rule Payload",
    'th_rule_topic_op_name': "Topic Operation",
    'th_rule_topic_op_args': "Topic Arguments",
    'th_rule_payload_op_name': "Payload Operation",
    'th_rule_payload_op_args': "Payload Arguments",

    # Options - Add rule
    'menu_op_add_rule': "Add Rule.",
    'prompt_add_rule': "Enter Rule: ",
    'info_rule_added': "Rule added: {}",
    'warning_empty_rule': "Empty rule, ignoring...",
    'warning_existing_rule': "Rule already exists, ignoring...",
    'error_invalid_rule': "Invalid rule format. Check syntax and data types.",

    # Options - Delete rule
    'menu_op_del_rule': "Delete Rule.",
    'prompt_del_rule': "Enter the rule number to delete: ",
    'warning_no_rules': "No rules to delete.",
    'info_rule_deleted': "Rule deleted: {}",
    'error_invalid_rule_number': "Invalid rule index.",

    # Options - Show credentials
    'menu_op_show_credentials': "Show Credentials.",
    'th_credential_client_id': "Client ID",
    'th_credential_username': "Username",
    'th_credential_password': "Password",

    # Options - Start MITM
    'menu_op_start_mitm': "Start MITM.",
    'starting_sniffer': "Starting sniffer.",
    'info_starting_sniffer': "Starting sniffer on interface '{}' with MAC address '{}' and port '{}'.",

    # Exit
    'menu_op_goodbye': "Exit.",
    'menu_goodbye': "Goodbye!",

    # Configuration check
    'menu_op_show_config': "Show Current Configuration.",
    'th_config': "Current Configuration",
    'warning_ifname_empty': "Interface name is empty.",
    'warning_lmac_empty': "Local MAC address is empty.",
    'warning_lmac_invalid': "Invalid MAC address: '{}'.",
    'warning_lmac_mismatch': "Local MAC address '{}' does not match the interface MAC address for '{}'.",
})

# Network notifications
MESSAGES.update({
    'info_getting_arp_table': "Getting ARP table...",
    'debug_arp_table': "ARP table: {}",
    'warning_arp_table_empty': "ARP table is empty or could not be retrieved.",
    'warning_interface_not_found': "Interface '{}' not found.",
    'warning_mac_address_not_found': "MAC address not found for interface '{}'",
})

# Sniffer and tampering notifications
MESSAGES.update({
    'debug_mqtt_packet_received': "MQTT '{}' from '{}'/'{}'/'{}' to '{}'/'{}'/'{}'.",
    'info_mqtt_rule_applied': "MQTT rule applied: ({}) '{}':'{}' -> '{}':'{}'.",
    'info_credentials_found': "Credentials found!: Client ID: '{}', Username: '{}', Password: '{}'",
})

# Generic info, warnings, and errors
MESSAGES.update({
    'info_operation_cancelled': "Operation cancelled by user.",
    'error_permission_denied': "Permission denied. Please run as administrator.",
})
