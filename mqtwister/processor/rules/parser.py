import re
from ast import literal_eval


def _get_item(token: str, item: str) -> str | None:
    match = re.search(rf'{item}="(.*)"', token)
    return match.group(1) if match else None


def _get_topic(token: str) -> str | None:
    return _get_item(token, 'topic')


def _get_payload(token: str) -> str | None:
    return _get_item(token, 'payload')


def _get_op(token: str, item: str) -> tuple[str | None, str | None]:

    op_name: str | None = None
    op_args: str | None = None

    match = re.search(rf'{item}\.(\w+)\((.*)\)', token)
    if match:
        op_name = match.group(1)
        if (op_args := match.group(2)):
            op_args = literal_eval(match.group(2))

    return (op_name, op_args)


def _get_topic_op(token: str) -> tuple[str | None, str | None]:

    return _get_op(token, 'topic')


def _get_payload_op(token: str) -> tuple[str | None, str | None]:

    return _get_op(token, 'payload')


def parse_tokens(tokens: list[str]) -> dict:

    values = {
        'topic': None,
        'payload': None,
        'topic_op': (None, None),
        'payload_op': (None, None),
    }

    for token in tokens:

        if token.startswith('topic='):
            values['topic'] = _get_topic(token)
        elif token.startswith('payload='):
            values['payload'] = _get_payload(token)
        elif token.startswith('topic.'):
            op_name, op_value = _get_topic_op(token)
            values['topic_op'] = (op_name, op_value)
        elif token.startswith('payload.'):
            op_name, op_value = _get_payload_op(token)
            values['payload_op'] = (op_name, op_value)

    return values
