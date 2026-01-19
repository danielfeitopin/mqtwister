from scapy.all import Packet
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, TCP
from scapy.contrib.mqtt import MQTT, MQTTPublish
from mqtwister.processor.rules import Rule
from mqtwister.processor import process_MQTTPublish

def get_MQTT_publish_packet(topic: bytes, payload: bytes) -> Packet:
    """Returns a new empty Scapy Packet instance with layers initialized."""
    return Ether()/IP()/TCP()/MQTT()/MQTTPublish(topic=topic, value=payload)

def get_rule_instance(rule_str: str) -> Rule:
    """Returns a new Rule instance initialized with the given rule string."""
    return Rule.from_str(rule_str)

def test_rule_matches():
    RULE_STR: str = 'topic="colors" payload.set_value("RED")'
    rule: Rule = get_rule_instance(RULE_STR)
    packet: Packet = get_MQTT_publish_packet(b"colors", b"blue")
    assert rule.matches(packet[MQTTPublish].topic, packet[MQTTPublish].value) is True


def test_rule_aply():
    
    RULE_STR: str = 'topic="test_op/replace" payload.replace("World", "Test")'
    rule: Rule = Rule.from_str(RULE_STR)
    packet: Packet = get_MQTT_publish_packet(b"test_op/replace", b"Hello, World!")
    process_MQTTPublish(packet, [rule])
    assert packet[MQTTPublish].value == b"Hello, Test!"