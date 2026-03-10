# SPDX-FileCopyrightText: 2026 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

import pytest
from mqtwister.processor.rules.parser import (
    _get_item,
    _get_topic,
    _get_payload,
    _get_op,
    parse_tokens
)

VALID_TOPIC = '/smile'
VALID_TOPIC_ASSIGNMENT = 'topic="/smile"'
VALID_PAYLOAD = ':)'
VALID_PAYLOAD_ASSIGNMENT = 'payload=":)"'


@pytest.mark.parametrize("item_type, token, expected", [

    # Valid assignments
    ('topic', VALID_TOPIC_ASSIGNMENT, VALID_TOPIC),
    ('payload', VALID_PAYLOAD_ASSIGNMENT, VALID_PAYLOAD),

    # Switched assignments
    ('topic', VALID_PAYLOAD_ASSIGNMENT, None),
    ('payload', VALID_TOPIC_ASSIGNMENT, None),
    
    # Mixed quotes
    ('item', 'item="value"', 'value'),
    ('item', "item='value'", 'value'),
    ('item', 'item="value\'s test"', "value's test"),
    ('item', "item='value\"s test'", 'value"s test'),
    ('item', 'item="mixed quotes\'', None),
    ('item', 'item=\'mixed quotes"', None),

])
def test_get_item(item_type, token, expected):
    assert _get_item(token, item_type) == expected


@pytest.mark.parametrize("token, expected", [

    # Test case with topic
    (VALID_TOPIC_ASSIGNMENT, VALID_TOPIC),

    # Test case without topic
    (VALID_PAYLOAD_ASSIGNMENT, None),
])
def test_get_topic(token, expected):
    assert _get_topic(token) == expected


@pytest.mark.parametrize("token, expected", [

    # Test case with payload
    (VALID_PAYLOAD_ASSIGNMENT, VALID_PAYLOAD),

    # Test case without payload
    (VALID_TOPIC_ASSIGNMENT, None)
])
def test_get_payload(token, expected):
    assert _get_payload(token) == expected


@pytest.mark.parametrize("item_type, token, expected", [

    # Test case on topic operator with operator
    ('topic', 'topic.append("/sad")', ('append', ('/sad',))),

    # Test case on topic operator without operator
    ('topic', 'payload.replace(")","(")', (None, None)),
    ('topic', 'topic="/smile")', (None, None)),

    # Test case on payload operator with operator
    ('payload', 'payload.replace(")","(")', ('replace', (')', '('))),

    # Test case on payload operator without operator
    ('payload', 'topic.append("/sad")', (None, None)),
    ('payload', 'payload=":)"', (None, None)),

])
def test_get_op(item_type, token, expected):
    assert _get_op(token, item_type) == expected

@pytest.mark.parametrize("tokens, expected", [
    (
        [
            'topic="/x"',
            'payload="x"',
            'topic.map("a","b")',
            'payload.replace("(",")")'
        ],
        {
            'topic': '/x',
            'payload': 'x',
            'topic_op': ('map', ('a', 'b')),
            'payload_op': ('replace', ('(', ')')),
        }
    )
])
def test_parse_tokens(tokens, expected):
    assert parse_tokens(tokens) == expected