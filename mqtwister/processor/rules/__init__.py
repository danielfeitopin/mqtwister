import re
from .tokenizer import tokenize
from .parser import parse_tokens


class Rule:
    def __init__(self, topic: str | None = None, payload: str | None = None,
                 topic_op: tuple[str | None, tuple | None] = (None, None),
                 payload_op: tuple[str | None, tuple | None] = (None, None)):

        self.topic: str | None = topic
        self.topic_pattern: re.Pattern | None = re.compile(topic.encode()) \
            if topic else None

        self.payload: str | None = payload
        self.payload_pattern: re.Pattern | None = re.compile(payload.encode()) \
            if payload else None

        self.topic_op_name: str | None = topic_op[0]
        self.topic_args_string: str = '(' \
            + ', '.join(repr(arg) for arg in topic_op[1] or ()) \
            + ')' if topic_op[0] else None

        self.payload_op_name: str | None = payload_op[0]
        self.payload_args_string: str = '(' \
            + ', '.join(repr(arg) for arg in payload_op[1] or ()) \
            + ')' if payload_op[0] else None

        # Encode string arguments for better efficiency in operations
        self.topic_op_args: tuple = tuple(
            item.encode() if isinstance(item, str) else item
            for item in topic_op[1]
        ) if topic_op[1] else ()

        self.payload_op_args: tuple = tuple(
            item.encode() if isinstance(item, str) else item
            for item in payload_op[1]
        ) if payload_op[1] else ()

    # Getters
    def get_topic(self) -> str | None:
        return self.topic

    def get_payload(self) -> str | None:
        return self.payload

    def get_topic_op_name(self) -> str | None:
        return self.topic_op_name

    def get_topic_op_args_string(self) -> str | None:
        return self.topic_args_string

    def get_topic_op_values(self) -> tuple | None:
        return self.topic_op_args

    def get_payload_op_name(self) -> str | None:
        return self.payload_op_name

    def get_payload_op_args_string(self) -> str | None:
        return self.payload_args_string

    def get_payload_op_values(self) -> tuple | None:
        return self.payload_op_args

    # Utility methods
    @classmethod
    def from_str(cls, rule_str: str) -> 'Rule':
        """Create a Rule object from a string."""

        return cls(**parse_tokens(tokenize(rule_str)))

    def matches(self, topic: bytes, payload: bytes) -> bool:
        """Check if the rule matches the given topic and payload."""

        topic_match: bool = bool(self.topic_pattern.match(topic)) \
            if self.topic_pattern else True

        payload_match: bool = bool(self.payload_pattern.match(payload)) \
            if self.payload_pattern else True

        return topic_match and payload_match

    def is_empty(self) -> bool:
        """Check if the rule is empty (no topic, no payload, no operations)."""
        return not (
            self.topic or self.payload
            or (self.topic_op_name, self.topic_op_args) != (None, None)
            or (self.payload_op_name, self.payload_op_args) != (None, None)
        )

    def __repr__(self):

        string: str = '<Rule: '

        if (v := self.get_topic()):
            string += f'topic="{v}"'

        if (v := self.get_payload()):
            string += f', payload="{v}"'

        if (v := self.get_topic_op_name()):
            string += f', topic_op="{v}{self.get_topic_op_args_string()}"'

        if (v := self.get_payload_op_name()):
            string += f', payload_op="{v}{self.get_payload_op_args_string()}"'

        string += '>'

        return string

    # Redefine equality and hash methods
    def __eq__(self, other):
        if not isinstance(other, Rule):
            return NotImplemented
        return (
            self.topic == other.topic
            and self.payload == other.payload
            and self.topic_op_name == other.topic_op_name
            and self.topic_op_args == other.topic_op_args
            and self.payload_op_name == other.payload_op_name
            and self.payload_op_args == other.payload_op_args
        )

    def __hash__(self):
        return hash((
            self.topic, self.payload,
            self.topic_op_name, self.topic_op_args,
            self.payload_op_name, self.payload_op_args
        ))
