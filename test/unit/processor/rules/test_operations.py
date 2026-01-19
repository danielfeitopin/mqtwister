import pytest
from mqtwister.processor.tampering.operations import (
    set_value, replace, swap, lowercase, uppercase, prepend, append, trim,
    truncate, to_int_str, to_float_str, encode_base64, decode_base64
)

TEST_VALUE: bytes = b"Hello, World!"


@pytest.mark.parametrize("function, parameters, expected", [
    (set_value, (TEST_VALUE, b"New Value"), b"New Value"),
    (replace, (TEST_VALUE, b"World", b"There"), b"Hello, There!"),
    (swap, (TEST_VALUE, b"Hello", b"World"), b"World, Hello!"),
    (lowercase, (TEST_VALUE,), b"hello, world!"),
    (uppercase, (TEST_VALUE,), b"HELLO, WORLD!"),
    (prepend, (TEST_VALUE, b"Hello "), b"Hello Hello, World!"),
    (append, (TEST_VALUE, b" Goodbye!"), b"Hello, World! Goodbye!"),
    (trim, (b"  Hello, World!  ",), b"Hello, World!"),
    (truncate, (TEST_VALUE, 5), b"Hello"),
    (to_int_str, (b"3",), "3"),
    (to_int_str, (b"3.14",), "3"),
    (to_float_str, (b"3",), "3.0"),
    (to_float_str, (b"3.14",), "3.14"),
    (encode_base64, (TEST_VALUE,), b"SGVsbG8sIFdvcmxkIQ=="),
    (decode_base64, (b"SGVsbG8sIFdvcmxkIQ==",), TEST_VALUE),
])
def test_operations(function, parameters, expected):
    assert function(*parameters) == expected
