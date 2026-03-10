# SPDX-FileCopyrightText: 2026 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

from scapy.layers.inet import IP, TCP
from scapy.contrib.mqtt import MQTT, MQTTPublish
from mqtwister.utils.logging import logger
from mqtwister.lang import get_message as m
from .operations import OPERATIONS


def call_operation(item: bytes, op_name: str, op_args: tuple) -> bytes:
    """
    Calls the operation function by name with the provided value and arguments.
    """

    try:

        # Call the operation function if it exists and return the result
        if op_func := OPERATIONS.get(op_name):
            return op_func(item, *op_args)
        else:
            logger.error(m('error_operation_not_found', op_name))
    except Exception as e:
        logger.error(m('error_operation_failed', op_name, e))

    # Return the original item if operation fails
    return item


def recalculate_MQTTPublish(packet: MQTTPublish) -> None:

    del packet[MQTTPublish].length
    del packet[MQTT].len
    del packet[TCP].chksum
    del packet[IP].len
    del packet[IP].chksum

    return None
