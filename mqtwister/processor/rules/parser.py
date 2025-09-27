import re
from ast import literal_eval


def _get_item(token: str, item: str) -> str | None:
    pattern = re.compile(rf'{item}=(["\'])(.*?)\1')
    match = pattern.fullmatch(token)
    return match.group(2) if match and len(match.groups()) > 1 else None


def _get_topic(token: str) -> str | None:
    return _get_item(token, 'topic')


def _get_payload(token: str) -> str | None:
    return _get_item(token, 'payload')


def _get_op(token: str, item: str) -> tuple[str | None, tuple | None]:

    pattern = re.compile(rf'{item}\.(\w+)\((.*)\)')
    op_name: str | None = None
    op_args: tuple | None = None

    match = pattern.search(token)
    if match:
        op_name = match.group(1)
        if (op_args := match.group(2)):
            op_args = literal_eval(match.group(2))
            if op_args and not isinstance(op_args, tuple):
                op_args = (op_args,)

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
