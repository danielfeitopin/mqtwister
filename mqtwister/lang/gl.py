# SPDX-FileCopyrightText: 2025 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

MESSAGES: dict[str, str] = {}

# Menu entries, prompts, and actions
MESSAGES.update({

    # Main menu
    'menu_prompt': "Introduza opción: ",
    'menu_invalid_choice': "Opción inválida, por favor intente de novo.",
    'th_menu': "MENÚ PRINCIPAL",

    # Options - Show ARP table
    'menu_op_show_arp_table': "Amosar táboa ARP.",
    'th_arp_table_ip': "Enderezo IP",
    'th_arp_table_mac': "Enderezo MAC",

    # Options - Show interfaces
    'menu_op_show_interfaces': "Amosar interfaces.",
    'th_interface_mac': "Enderezo MAC",
    'th_interface_name': "Nome da interface",

    # Options - Set MAC address
    'menu_op_set_lmac': "Establecer enderezo MAC local.",
    'prompt_set_lmac': "Introduza o enderezo MAC local: ",
    'info_set_lmac': "Enderezo MAC establecido a '{}'.",

    # Options - Set interface name
    'menu_op_set_ifname': "Establecer nome da interface.",
    'prompt_set_ifname': "Introduza o nome da interface: ",
    'info_set_ifname': "Nome da interface establecido a '{}'.",

    # Options - Set listening port
    'menu_op_set_port': "Establecer porto de escoita.",
    'prompt_set_port': "Introduza o porto a escoitar (por defecto 1883): ",
    'info_set_port': "Porto de escoita establecido a '{}'.",
    'error_invalid_port': "Número de porto inválido. Por favor, introduza un porto válido entre 1 e 65535.",

    # Options - Show rules
    'menu_op_show_rules': "Amosar regras.",
    'th_rule_topic': "Topic da regra",
    'th_rule_payload': "Payload da regra",
    'th_rule_topic_op_name': "Operación de Topic",
    'th_rule_topic_op_args': "Argumentos de Topic",
    'th_rule_payload_op_name': "Operación de Payload",
    'th_rule_payload_op_args': "Argumentos de Payload",

    # Options - Add rule
    'menu_op_add_rule': "Agregar regra.",
    'prompt_add_rule': "Introduza a regra: ",
    'info_rule_added': "Regra agregada: {}",
    'warning_empty_rule': "Regra vacía, ignorando...",
    'warning_existing_rule': "A regra xa existe, ignorando...",
    'error_invalid_rule': "Formato de regra inválido. Verifique a sintaxe e os tipos de datos.",

    # Options - Delete rule
    'menu_op_del_rule': "Borrar regra.",
    'prompt_del_rule': "Introduza o número de regra a eliminar: ",
    'warning_no_rules': "Non hai regras para eliminar.",
    'info_rule_deleted': "Regra eliminada: {}",
    'error_invalid_rule_number': "Índice de regra inválido.",

    # Options - Show credentials
    'menu_op_show_credentials': "Amosar credenciais.",
    'th_credential_client_id': "ID de cliente",
    'th_credential_username': "Nome de usuario",
    'th_credential_password': "Contrasinal",

    # Options - Start MITM
    'menu_op_start_mitm': "Iniciar MITM.",
    'starting_sniffer': "Iniciando sniffer.",
    'info_starting_sniffer': "Iniciando sniffer na interface '{}' con enderezo MAC '{}' e porto '{}'.",

    # Exit
    'menu_op_goodbye': "Saír.",
    'menu_goodbye': "Adeus!",

    # Configuration check
    'menu_op_show_config': "Amosar configuración actual.",
    'th_config': "Configuración actual",
    'warning_ifname_empty': "O nome da interface está baleiro.",
    'warning_lmac_empty': "O enderezo MAC local está baleiro.",
    'warning_lmac_invalid': "Enderezo MAC inválido: '{}'.",
    'warning_lmac_mismatch': "O enderezo MAC local '{}' non coincide co enderezo MAC da interface para '{}'.",
})

# Network notifications
MESSAGES.update({
    'info_getting_arp_table': "Obtendo táboa ARP...",
    'warning_arp_table_empty': "A táboa ARP está baleira ou non se puido recuperar.",
    'warning_interface_not_found': "Interface '{}' non atopada.",
    'warning_mac_address_not_found': "Enderezo MAC non atopado para a interface '{}'",
    'error_retrieving_arp_table': "Erro ao recuperar a táboa ARP: {}",
    'error_arp_table_retrieval_not_implemented': "A recuperación da táboa ARP non está implementada para este sistema operativo.",
})

# Tampering notifications
MESSAGES.update({
    'debug_mqtt_packet_received': "Paquete MQTT recibido de '{}'/'{}'/'{}' a '{}'/'{}'/'{}'.",
    'info_mqtt_rule_match': "{} coincide con '{}':'{}'.",
    'info_mqtt_rule_applied': "Substitución aplicada: '{}':'{}' -> '{}':'{}'.",
    'info_credentials_found': "Credenciais atopadas!: ID de cliente: '{}', Nome de usuario: '{}', Contrasinal: '{}'",
    'error_operation_failed': "A operación '{}' fallou: {}",
    'error_operation_not_found': "Operación '{}' non atopada.",
})

# Generic info, warnings, and errors
MESSAGES.update({
    'info_operation_cancelled': "Operación cancelada polo usuario.",
    'error_permission_denied': "Permiso denegado. Por favor, execute como administrador.",
})
