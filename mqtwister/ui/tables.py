# SPDX-FileCopyrightText: 2025 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

COLUMN_PADDING: int = 1
SEPARATOR: str = '|'
DELIMITER: str = '='
HEADER_SEPARATOR: str = '-'

def make_table(rows: list[tuple[str]], headers: list[str] = None) -> str:
    """Create the tables for the CLI."""

    # Calculate the widths of each column based on data
    widths: list[int] = [
        max(len(str(item)) for item in column) for column in zip(*rows)
    ]

    # If headers are provided, adjust widths accordingly
    if headers:
        
        # Extend widths if headers are longer than data columns
        if len(headers) > len(widths):
            widths.extend([0] * (len(headers) - len(widths)))
        
        # Update widths based on headers
        for i in range(len(headers)):
            widths[i] = max(widths[i], len(headers[i]))

    # Adjust widths for padding
    widths = [w + COLUMN_PADDING * 2 for w in widths]

    # Calculate the total width of the table
    table_width: int = sum(widths) + len(SEPARATOR) * (len(widths) - 1)

    # Start building the table string
    table: str = f"{DELIMITER * table_width}\n"

    # Create the header row if headers are provided
    if headers:
        table += SEPARATOR.join(th.center(w) for th, w in zip(headers, widths))
        table += f"\n{HEADER_SEPARATOR * table_width}\n"

    # Create the data rows
    for row in rows:
        table += SEPARATOR.join(str(i).center(w) for i, w in zip(row, widths))
        table += '\n'

    # Add the closing line
    table += f"{DELIMITER * table_width}"

    return table
