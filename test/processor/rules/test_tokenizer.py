import pytest
from mqtwister.processor.rules.tokenizer import tokenize

@pytest.mark.parametrize("input_line, expected_tokens", [
    # Simple key-value pair
    ('topic="/temp"', ['topic="/temp"']),

    # Multiple key-value pairs
    ('topic="/temp" payload="25C"', ['topic="/temp"', 'payload="25C"']),

    # Function with no arguments
    ('payload.clear()', ['payload.clear()']),

    # Function with single argument
    ('topic.append(/sad)', ['topic.append(/sad)']),

    # Function with string arguments
    ('payload.replace("C","F")', ['payload.replace("C","F")']),

    # Function with space and comma inside argument
    ('payload.replace(" ) ,(")', ['payload.replace(" ) ,(")']),

    # Mixed tokens: key-value and function
    (
        'topic="/smile" payload=":)" payload.replace(" ) ,(")',
        ['topic="/smile"', 'payload=":)"', 'payload.replace(" ) ,(")']
    ),

    # Function with parentheses inside string argument
    ('payload.replace("start(", "end)")', ['payload.replace("start(", "end)")']),

    # Escaped quotes inside function arguments
    ('payload.replace(\\"A\\",\\"B\\")', ['payload.replace(\\"A\\",\\"B\\")']),

    # Extra spaces between tokens
    (
        '   topic="/data"   payload="ok"   ',
        ['topic="/data"', 'payload="ok"']
    ),

    # Complex combination of functions and key-value pairs
    (
        'topic="/x" payload="x" topic.map(a,b) payload.replace("(",")")',
        ['topic="/x"', 'payload="x"', 'topic.map(a,b)', 'payload.replace("(",")")']
    )
])
def test_tokenizer(input_line, expected_tokens):
    assert tokenize(input_line) == expected_tokens
