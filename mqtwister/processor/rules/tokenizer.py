def tokenize(line: str) -> list[str]:

    tokens: list[str] = []  # List to hold the final tokens
    current: str = ''  # Current token being built
    in_string: bool = False  # Whether 'current' is inside a string
    escape: bool = False  # Whether the next character is escaped
    paren_depth: int = 0  # Current depth of parentheses
    quote_char: str = ''  # Single or double quote character

    for char in line:

        # Handle escaped characters
        if escape:
            current += char
            escape = False
            continue
        elif char == '\\':
            current += char
            escape = True
            continue
        
        # Handle string delimiters
        if char in ('"', "'"):
            current += char
            if in_string and char == quote_char:
                in_string = False
            elif not in_string:
                in_string = True
                quote_char = char
            continue
        elif in_string:
            current += char
            continue

        # Handle parentheses
        if char == '(':
            paren_depth += 1
        elif char == ')':
            paren_depth -= 1

        if char.isspace() and paren_depth == 0:
            if current:
                tokens.append(current.strip())
                current = ''
        else:
            current += char

    if current:
        tokens.append(current.strip())

    return tokens
