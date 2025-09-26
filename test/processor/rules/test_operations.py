import pytest
from mqtwister.processor.tampering.operations import (
    uppercase, lowercase, trim, replace, prepend, append, to_int, to_float
)


def test_uppercase():
    assert uppercase(b"hello") == b"HELLO"


def test_lowercase():
    assert lowercase(b"HELLO") == b"hello"


def test_trim():
    assert trim(b"  hello  ") == b"hello"


def test_replace():
    assert replace(b"hello world", b"world", b"there") == b"hello there"


def test_prepend():
    assert prepend(b"world", b"hello ") == b"hello world"


def test_append():
    assert append(b"hello", b" world") == b"hello world"


def test_to_int():
    assert to_int(b"123") == 123
    with pytest.raises(ValueError):
        to_int(b"abc")


def test_to_float():
    assert to_float(b"123.45") == 123.45
    with pytest.raises(ValueError):
        to_float(b"abc")
