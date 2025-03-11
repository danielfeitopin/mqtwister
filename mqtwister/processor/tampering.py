from scapy.contrib.mqtt import MQTTPublish


def value_to_zero(topic: bytes, value: bytes) -> tuple[bytes, bytes]:
    return (topic, b'0')


def value_to_zeros(topic: bytes, value: bytes) -> tuple[bytes, bytes]:
    return (topic, b'0'*len(value))


def alter_MQTTPublish_packet(packet: MQTTPublish,
                             function: 'function' = None) -> None:

    if function is not None:

        # Get MQTT topic and message
        topic: bytes = packet[MQTTPublish].topic
        value: bytes = packet[MQTTPublish].value

        # Modify MQTT topic and message
        new_topic, new_value = function(topic, value)
        packet[MQTTPublish].topic = new_topic
        packet[MQTTPublish].value = new_value

        msg: str = f"Message MQTT [topic:message]: "
        msg += f"{topic.decode()}:{value.decode()} -> "
        msg += f"{new_topic.decode()}:{new_value.decode()}"
        print(msg)

    return None
