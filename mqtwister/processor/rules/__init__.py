import re
from .tokenizer import tokenize
from .parser import parse_tokens


class Rule:
    def __init__(self, topic: str | None = None, payload: str | None = None,
                 topic_op: tuple[str | None, tuple | None] = (None, None),
                 payload_op: tuple[str | None, tuple | None] = (None, None)):

        self.topic: str | None = topic
        self.topic_bytes: bytes = topic.encode() if topic else b''

        self.payload: str | None = payload
        self.payload_bytes: bytes = payload.encode() if payload else b''

        self.topic_op: tuple[str | None, tuple | None] = topic_op
        self.payload_op: tuple[str | None, tuple | None] = payload_op

    # Getters
    def get_topic(self) -> str | None:
        return self.topic

    def get_payload(self) -> str | None:
        return self.payload

    def get_topic_op_name(self) -> str | None:
        return self.topic_op[0]

    def get_topic_op_values(self) -> tuple | None:
        return self.topic_op[1]

    def get_payload_op_name(self) -> str | None:
        return self.payload_op[0]

    def get_payload_op_values(self) -> tuple | None:
        return self.payload_op[1]

    # Utility methods
    @classmethod
    def from_str(cls, rule_str: str) -> 'Rule':
        """Create a Rule object from a string."""

        return cls(**parse_tokens(tokenize(rule_str)))

    def matches(self, topic: bytes, payload: bytes) -> bool:
        """Check if the rule matches the given topic and payload."""
        topic_match: bool = True
        payload_match: bool = True

        if self.topic_bytes:
            topic_match = re.match(self.topic_bytes, topic) is not None

        if self.payload_bytes:
            payload_match = re.match(self.payload_bytes, payload) is not None

        return topic_match and payload_match

    def is_empty(self) -> bool:
        """Check if the rule is empty (no topic, no payload, no operations)."""
        return not (self.topic or self.payload or
                    (self.topic_op != (None, None)) or
                    (self.payload_op != (None, None)))

    def __repr__(self):

        string: str = '<Rule: '

        if (v := self.get_topic()):
            string += f'topic="{v}"'

        if (v := self.get_payload()):
            string += f', payload="{v}"'

        if (v := self.get_topic_op_name()):
            args: tuple | None = self.get_topic_op_values()
            args: str = ', '.join(repr(arg) for arg in args) if args else ''
            string += f', topic_op="{v}({args})"'

        if (v := self.get_payload_op_name()):
            args: tuple | None = self.get_payload_op_values()
            args: str = ', '.join(repr(arg) for arg in args) if args else ''
            string += f', payload_op="{v}({args})"'

        string += '>'

        return string

    # Redefine equality and hash methods
    def __eq__(self, other):
        if not isinstance(other, Rule):
            return NotImplemented
        return (self.topic == other.topic and
                self.payload == other.payload and
                self.topic_op == other.topic_op and
                self.payload_op == other.payload_op)

    def __hash__(self):
        return hash((self.topic, self.payload, self.topic_op, self.payload_op))
