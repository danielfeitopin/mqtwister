from mqtwister.processor.rules import Rule
from typing import Callable

# Generic operation
def operation(topic: bytes | None = None, payload: bytes | None = None, rule: Rule = None) -> tuple[bytes | None, bytes | None]:
    """
    Generic operation that returns the topic and payload as is.
    This can be used as a placeholder for operations that do not modify the values.
    """
    return topic, payload

def uppercase(value: bytes) -> bytes:
    """Convierte el valor a mayúsculas si es bytes."""
    return value.upper()

def lowercase(value: bytes) -> bytes:
    """Convierte el valor a minúsculas si es bytes."""
    return value.lower()

def trim(value: bytes) -> bytes:
    """Elimina espacios al inicio y final si es bytes."""
    return value.strip()

def replace(value: bytes, old: bytes, new: bytes) -> bytes:
    """Reemplaza subcadenas en el valor si es bytes."""
    return value.replace(old, new)

def add_prefix(value: bytes, prefix: bytes) -> bytes:
    """Agrega un prefijo al valor si es bytes."""
    return prefix + value

def add_suffix(value: bytes, suffix: bytes) -> bytes:
    """Agrega un sufijo al valor si es bytes."""
    return value + suffix

def to_int(value: bytes) -> int:
    """Convierte el valor a entero si es posible."""
    try:
        return int(value.decode())
    except (ValueError, TypeError):
        raise ValueError(f"Cannot convert {value} to int")

def to_float(value: bytes) -> float:
    """Convierte el valor a flotante si es posible."""
    try:
        return float(value.decode())
    except (ValueError, TypeError):
        raise ValueError(f"Cannot convert {value} to float")

def truncate(value: bytes, length: int) -> bytes:
    """Truncates the value to the specified length if it is bytes."""
    return value[:length]

def swap(value: bytes, part1: bytes, part2: bytes) -> bytes:
    """Swaps occurrences of part1 with part2 in the value if it is bytes."""
    return value.replace(part1, b"TEMP_SWAP").replace(part2, part1).replace(b"TEMP_SWAP", part2)

def encode_base64(value: bytes) -> bytes:
    """Encodes the value in base64 if it is bytes."""
    import base64
    return base64.b64encode(value)

def decode_base64(value: bytes) -> bytes:
    """Decodes the value from base64 if it is bytes."""
    import base64
    try:
        return base64.b64decode(value)
    except (ValueError, TypeError):
        raise ValueError(f"Cannot decode {value} from base64")

OPERATIONS: dict[str, Callable[[bytes], bytes]] = {
    "uppercase": uppercase,
    "lowercase": lowercase,
    "trim": trim,
    "replace": replace,
    "add_prefix": add_prefix,
    "add_suffix": add_suffix,
    "to_int": to_int,
    "to_float": to_float,
    "truncate": truncate,
    "swap": swap,
    "encode_base64": encode_base64,
    "decode_base64": decode_base64,
}