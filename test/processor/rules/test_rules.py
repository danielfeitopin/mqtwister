import pytest
from mqtwister.processor.rules import Rule
from mqtwister.processor.rules.parser import parse_tokens


@pytest.mark.parametrize("topic, payload, topic_op, payload_op", [
    ("test_topic", "test_payload", ("contains", "value"), (None, None)),
    ("another_topic", "another_payload", (None, None), ("replace", "new_value")),
])
def test_rule_creation(topic, payload, topic_op, payload_op):
    rule = Rule(topic=topic, payload=payload,
                topic_op=topic_op, payload_op=payload_op)
    assert rule.topic == topic
    assert rule.payload == payload
    assert rule.topic_op == topic_op
    assert rule.payload_op == payload_op


@pytest.mark.parametrize("rule, expected_repr", [
    (
        Rule(
            topic="test_topic",
            payload="test_payload",
            topic_op=("contains", "value"),
            payload_op=(None, None)
        ),
        "<Rule: topic=\"test_topic\", payload=\"test_payload\", " \
            + "topic_op=\"('contains', 'value')\", " \
            + "payload_op=\"(None, None)\">"
    ),
    (
        Rule(
            topic="another_topic",
            payload="another_payload",
            topic_op=(None, None),
            payload_op=("replace", "new_value")
        ),
        "<Rule: topic=\"another_topic\", payload=\"another_payload\", " \
            + "topic_op=\"(None, None)\", " \
            + "payload_op=\"('replace', 'new_value')\">"
    )
])
def test_rule_repr(rule, expected_repr):
    assert repr(rule) == expected_repr


@pytest.mark.parametrize("rule1, rule2, are_equal", [
    (Rule("test_topic", "test_payload", ("contains", "value"), (None, None)),
     Rule("test_topic", "test_payload", ("contains", "value"), (None, None)), True),
    (Rule("test_topic", "test_payload", ("contains", "value"), (None, None)),
     Rule("different_topic", "test_payload", ("contains", "value"), (None, None)), False),
])
def test_rule_equality(rule1, rule2, are_equal):
    assert (rule1 == rule2) == are_equal


@pytest.mark.parametrize("line, expected_rule", [
    ('topic="test_topic" payload="test_payload"',
     Rule(topic="test_topic", payload="test_payload")),

    ('topic="test_topic" payload="test_payload" topic.contains("value")',
     Rule(topic="test_topic", payload="test_payload", topic_op=("contains", "value"))),

    ('topic="value with \\"escaped quotes\\"" payload="simple payload"',
     Rule(topic='value with \\"escaped quotes\\"', payload="simple payload")),

    ('invalid rule line',
     Rule()),
])
def test_rule_from_str(line, expected_rule):
    result = Rule.from_str(line)
    assert result == expected_rule
