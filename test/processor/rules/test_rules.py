import pytest
import re
from mqtwister.processor.rules import Rule


@pytest.mark.parametrize("topic, payload, topic_op, payload_op", [
    ("test_topic", "test_payload", ("contains", ("value",)), (None, None)),
    ("another_topic", "another_payload", (None, None), ("replace", ("new_value",))),
])
def test_rule_creation(topic, payload, topic_op, payload_op):
    rule = Rule(topic=topic, payload=payload,
                topic_op=topic_op, payload_op=payload_op)
    assert rule.topic == topic == rule.get_topic()
    assert rule.topic_pattern == (
        re.compile(topic.encode()) if topic else None)
    assert rule.payload == payload == rule.get_payload()
    assert rule.payload_pattern == (re.compile(
        payload.encode()) if payload else None)
    assert rule.get_topic_op_name() == topic_op[0]
    assert rule.get_payload_op_name() == payload_op[0]
    assert rule.get_topic_op_values() == (
        tuple(
            item.encode() if isinstance(item, str) else item
            for item in topic_op[1]
        ) if topic_op[1] else ()
    )
    assert rule.get_payload_op_values() == (
        tuple(
            item.encode() if isinstance(item, str) else item
            for item in payload_op[1]
        ) if payload_op[1] else ()
    )


@pytest.mark.parametrize("rule, expected_repr", [
    (
        Rule(
            topic="test_topic",
            payload="test_payload",
            topic_op=("contains", ("value",)),
            payload_op=(None, None)
        ),
        "<Rule: topic=\"test_topic\", payload=\"test_payload\", "
        + "topic_op=\"contains('value')\">"
    ),
    (
        Rule(
            topic="another_topic",
            payload="another_payload",
            topic_op=(None, None),
            payload_op=("replace", ("new_value",))
        ),
        "<Rule: topic=\"another_topic\", payload=\"another_payload\", "
        + "payload_op=\"replace('new_value')\">"
    )
])
def test_rule_repr(rule, expected_repr):
    assert repr(rule) == expected_repr


@pytest.mark.parametrize("rule1, rule2, are_equal", [
    (Rule("test_topic", "test_payload", ("contains", ("value",)), (None, None)),
     Rule("test_topic", "test_payload", ("contains", ("value",)), (None, None)), True),
    (Rule("test_topic", "test_payload", ("contains", ("value",)), (None, None)),
     Rule("different_topic", "test_payload", ("contains", ("value",)), (None, None)), False),
])
def test_rule_equality(rule1, rule2, are_equal):
    assert (rule1 == rule2) == are_equal


@pytest.mark.parametrize("line, expected_rule", [
    ('topic="test_topic" payload="test_payload"',
     Rule(topic="test_topic", payload="test_payload")),

    ('topic="test_topic" payload="test_payload" topic.contains("value")',
     Rule(topic="test_topic", payload="test_payload", topic_op=("contains", ("value",)))),

    ('topic="value with \\"escaped quotes\\"" payload="simple payload"',
     Rule(topic='value with \\"escaped quotes\\"', payload="simple payload")),

    ('invalid rule line',
     Rule()),

    ('topic="/x" payload="x" topic.map("a","b") payload.replace("(",")")',
     Rule(topic="/x", payload="x", topic_op=("map", ("a", "b")), payload_op=("replace", ("(", ")"))))
])
def test_rule_from_str(line, expected_rule):
    result = Rule.from_str(line)
    assert result == expected_rule


@pytest.mark.parametrize("rule, topic, payload, matches", [

    # Rule matches both topic and payload
    (Rule(topic="test/topic", payload="test_payload"),
     b"test/topic", b"test_payload", True),

    # Rule matches topic but not payload
    (Rule(topic="test/topic", payload="test_payload"),
     b"test/topic", b"different_payload", False),

    # Rule matches payload but not topic
    (Rule(topic="test/topic", payload="test_payload"),
     b"different/topic", b"test_payload", False),

    # Rule matches neither topic nor payload
    (Rule(topic="test/topic", payload="test_payload"),
     b"different/topic", b"different_payload", False),

    # Rule with no topic or payload matches any input
    (Rule(),
     b"any/topic", b"any_payload", True),

    # Rule with only topic matches topic
    (Rule(topic="test/topic"),
     b"test/topic", b"any_payload", True),

    # Rule with only payload matches payload
    (Rule(payload="test_payload"),
     b"any/topic", b"test_payload", True),
])
def test_rule_matches(rule, topic, payload, matches):
    assert rule.matches(topic, payload) == matches
