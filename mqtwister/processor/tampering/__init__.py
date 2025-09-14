# SPDX-FileCopyrightText: 2025 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

from .operations import OPERATIONS


def call_operation(item: bytes, op_name: str, op_args: tuple) -> bytes:
    """
    Calls the operation function by name with the provided value and arguments.
    """

    # Set default new value to the original item
    new_value: bytes = item

    try:

        # Call the operation function if it exists
        if op_func := OPERATIONS.get(op_name):
            new_value = op_func(item, *op_args)

    except:

        # If operation fails, keep the original value
        pass

    return new_value