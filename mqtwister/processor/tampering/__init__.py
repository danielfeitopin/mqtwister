# SPDX-FileCopyrightText: 2025 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

from scapy.contrib.mqtt import MQTTPublish
from mqtwister.processor.rules import Rule
from mqtwister.processor.tampering.operations import call_operation


def alter_MQTTPublish_packet(packet: MQTTPublish, rules: list[Rule]) -> None:

    # Get MQTT topic and message
    topic: bytes = packet[MQTTPublish].topic
    payload: bytes = packet[MQTTPublish].value

    # Match and apply rules
    for rule in rules:

        if rule.matches(topic, payload):

            # Set default new values
            new_topic: bytes = topic
            new_payload: bytes = payload

            # Apply operations
            if topic_op := rule.get_topic_op_name():
                args: tuple = rule.get_topic_op_values() or ()
                new_topic: bytes = call_operation(topic, topic_op, args)
                packet[MQTTPublish].topic = new_topic

            if payload_op := rule.get_payload_op_name():
                args: tuple = rule.get_payload_op_values() or ()
                new_payload: bytes = call_operation(payload, payload_op, args)
                packet[MQTTPublish].value = new_payload

            # Print message
            msg: str = f"Message MQTT [topic:message]: " \
                + f"{topic.decode()}:{payload.decode()} -> " \
                + f"{new_topic.decode()}:{new_payload.decode()}"
            print(msg)

            break

    return None
