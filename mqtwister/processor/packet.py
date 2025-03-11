from scapy.all import Packet, NoPayload
from scapy.layers.inet import IP, TCP


def get_layers(packet: Packet) -> list[Packet]:

    layer: Packet = packet
    layers: list[Packet] = []
    while layer != NoPayload():
        current_layer: Packet = layer.copy()
        current_layer.payload = NoPayload()
        # current_layer.show()
        layers.append(current_layer)
        layer = layer.payload

    return layers


def reassemble_packet(layers: list[Packet]) -> Packet:

    reassembled_packet: Packet | None = None
    for layer in layers:
        if reassembled_packet is None:
            reassembled_packet: Packet = layer
        else:
            reassembled_packet /= layer

    return reassembled_packet


def recalculate_values(packet: TCP) -> None:

    del packet[TCP].chksum
    del packet[IP].len
    del packet[IP].chksum

    return None
