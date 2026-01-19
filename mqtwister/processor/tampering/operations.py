import base64
from typing import Callable


def set_value(value: bytes, new_value: bytes) -> bytes:
    return new_value


def replace(value: bytes, old: bytes, new: bytes, count: int = -1) -> bytes:
    """Reemplaza subcadenas en el valor si es bytes."""
    return value.replace(old, new, count)


def swap(value: bytes, part1: bytes, part2: bytes) -> bytes:
    """Swaps occurrences of part1 with part2 in the value if it is bytes."""
    return value.replace(part1, b"TEMP_SWAP").replace(part2, part1).replace(b"TEMP_SWAP", part2)


def lowercase(value: bytes) -> bytes:
    """Convierte el valor a minúsculas si es bytes."""
    return value.lower()


def uppercase(value: bytes) -> bytes:
    """Convierte el valor a mayúsculas si es bytes."""
    return value.upper()


def prepend(value: bytes, prefix: bytes) -> bytes:
    """Agrega un prefijo al valor si es bytes."""
    return prefix + value


def append(value: bytes, suffix: bytes) -> bytes:
    """Agrega un sufijo al valor si es bytes."""
    return value + suffix


def trim(value: bytes) -> bytes:
    """Elimina espacios al inicio y final si es bytes."""
    return value.strip()


def truncate(value: bytes, length: int) -> bytes:
    """Truncates the value to the specified length if it is bytes."""
    return value[:length]


def to_int_str(value: bytes) -> bytes:
    """Convierte el valor a entero si es posible."""
    try:
        return str(int(float(value))).encode()
    except (ValueError, TypeError):
        raise ValueError(f"Cannot convert {value} to int")


def to_float_str(value: bytes) -> bytes:
    """Convierte el valor a flotante si es posible."""
    try:
        return str(float(value)).encode()
    except (ValueError, TypeError):
        raise ValueError(f"Cannot convert {value} to float")


def encode_base64(value: bytes) -> bytes:
    """Encodes the value in base64 if it is bytes."""

    return base64.b64encode(value)


def decode_base64(value: bytes) -> bytes:
    """Decodes the value from base64 if it is bytes."""

    try:
        return base64.b64decode(value)
    except (ValueError, TypeError):
        raise ValueError(f"Cannot decode {value} from base64")


OPERATIONS: dict[str, Callable] = {
    'set': set_value,
    'replace': replace,
    'swap': swap,
    'lowercase': lowercase,
    'uppercase': uppercase,
    'prepend': prepend,
    'append': append,
    'trim': trim,
    'truncate': truncate,
    'to_int_str': to_int_str,
    'to_float_str': to_float_str,
    'encode_base64': encode_base64,
    'decode_base64': decode_base64,
}
