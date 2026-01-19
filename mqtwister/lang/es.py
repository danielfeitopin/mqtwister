# SPDX-FileCopyrightText: 2025 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

MESSAGES: dict[str, str] = {}

# Menu entries, prompts, and actions
MESSAGES.update({

    # Main menu
    'menu_prompt': "Introduzca opción: ",
    'menu_invalid_choice': "Opción inválida, por favor intente de nuevo.",
    'th_menu': "MENÚ PRINCIPAL",

    # Options - Show ARP table
    'menu_op_show_arp_table': "Mostrar tabla ARP.",
    'th_arp_table_ip': "Dirección IP",
    'th_arp_table_mac': "Dirección MAC",

    # Options - Show interfaces
    'menu_op_show_interfaces': "Mostrar interfaces.",
    'th_interface_mac': "Dirección MAC",
    'th_interface_name': "Nombre de la interfaz",

    # Options - Set MAC address
    'menu_op_set_lmac': "Establecer dirección MAC local.",
    'prompt_set_lmac': "Introduzca la dirección MAC local: ",
    'info_set_lmac': "Dirección MAC establecida a '{}'.",

    # Options - Set interface name
    'menu_op_set_ifname': "Establecer nombre de la interfaz.",
    'prompt_set_ifname': "Introduzca el nombre de la interfaz: ",
    'info_set_ifname': "Nombre de la interfaz establecido a '{}'.",

    # Options - Set listening port
    'menu_op_set_port': "Establecer puerto de escucha.",
    'prompt_set_port': "Introduzca el puerto a escuchar (por defecto 1883): ",
    'info_set_port': "Puerto de escucha establecido a '{}'.",
    'error_invalid_port': "Número de puerto inválido. Por favor, introduzca un puerto válido entre 1 y 65535.",

    # Options - Show rules
    'menu_op_show_rules': "Mostrar reglas.",
    'th_rule_topic': "Topic de la regla",
    'th_rule_payload': "Payload de la regla",
    'th_rule_topic_op_name': "Operación de Topic",
    'th_rule_topic_op_args': "Argumentos de Topic",
    'th_rule_payload_op_name': "Operación de Payload",
    'th_rule_payload_op_args': "Argumentos de Payload",

    # Options - Add rule
    'menu_op_add_rule': "Agregar regla.",
    'prompt_add_rule': "Introduzca la regla: ",
    'info_rule_added': "Regla agregada: {}",
    'warning_empty_rule': "Regla vacía, ignorando...",
    'warning_existing_rule': "La regla ya existe, ignorando...",
    'error_invalid_rule': "Formato de regla inválido. Verifique la sintaxis y los tipos de datos.",

    # Options - Delete rule
    'menu_op_del_rule': "Borrar regla.",
    'prompt_del_rule': "Introduzca el número de regla a eliminar: ",
    'warning_no_rules': "No hay reglas para eliminar.",
    'info_rule_deleted': "Regla eliminada: {}",
    'error_invalid_rule_number': "Índice de regla inválido.",

    # Options - Show credentials
    'menu_op_show_credentials': "Mostrar credenciales.",
    'th_credential_client_id': "ID de cliente",
    'th_credential_username': "Nombre de usuario",
    'th_credential_password': "Contraseña",

    # Options - Start MITM
    'menu_op_start_mitm': "Iniciar MITM.",
    'starting_sniffer': "Iniciando sniffer.",
    'info_starting_sniffer': "Iniciando sniffer en la interfaz '{}' con dirección MAC '{}' y puerto '{}'.",

    # Exit
    'menu_op_goodbye': "Salir.",
    'menu_goodbye': "¡Adiós!",

    # Configuration check
    'menu_op_show_config': "Mostrar configuración actual.",
    'th_config': "Configuración actual",
    'warning_ifname_empty': "El nombre de la interfaz está vacío.",
    'warning_lmac_empty': "La dirección MAC local está vacía.",
    'warning_lmac_invalid': "Dirección MAC inválida: '{}'.",
    'warning_lmac_mismatch': "La dirección MAC local '{}' no coincide con la dirección MAC de la interfaz para '{}'.",
})

# Network notifications
MESSAGES.update({
    'info_getting_arp_table': "Obteniendo tabla ARP...",
    'warning_arp_table_empty': "La tabla ARP está vacía o no se pudo recuperar.",
    'warning_interface_not_found': "Interfaz '{}' no encontrada.",
    'warning_mac_address_not_found': "Dirección MAC no encontrada para la interfaz '{}'",
    'error_retrieving_arp_table': "Error al recuperar la tabla ARP: {}",
    'error_arp_table_retrieval_not_implemented': "La recuperación de la tabla ARP no está implementada para este sistema operativo.",
})

# Tampering notifications
MESSAGES.update({
    'debug_mqtt_packet_received': "Paquete MQTT recibido de '{}'/'{}'/'{}' a '{}'/'{}'/'{}'.",
    'info_mqtt_rule_match': "{} coincide con {}:{}.",
    'info_mqtt_rule_applied': "Substitución aplicada: '{}':'{}' -> '{}':'{}'.",
    'info_credentials_found': "¡Credenciales encontradas!: ID de cliente: '{}', Nombre de usuario: '{}', Contraseña: '{}'",
    'error_operation_failed': "La operación '{}' falló: {}",
    'error_operation_not_found': "Operación '{}' no encontrada.",
})

# Generic info, warnings, and errors
MESSAGES.update({
    'info_operation_cancelled': "Operación cancelada por el usuario.",
    'error_permission_denied': "Permiso denegado. Por favor, ejecute como administrador.",
})
