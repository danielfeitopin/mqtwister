# SPDX-FileCopyrightText: 2025 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

class Banner:

    LINES: list[str] = [
        r" __  __  ___ _____          _    _____         ",
        r"|  \/  |/ _ \_   _|_      _(_)__|_   _|__ _ __ ",
        r"| |\/| | | | || | \ \ /\ / / / __|| |/ _ \ '__|",
        r"| |  | | |_| || |  \ V  V /| \__ \| |  __/ |   ",
        r"|_|  |_|\__\_\|_|   \_/\_/ |_|___/|_|\___|_|   ",
    ]

    HEIGTH: int = len(LINES)
    WIDTH: int = len(LINES[0])
    TEXT: str = '\n'.join(LINES)
    DEFAULT_COLOR: int = 214

    @classmethod
    def get_colorful_banner(cls, color_256: int | None = None) -> str:
        if color_256 is None:
            decorator: str = f'\033[1m'
        else:
            decorator: str = f'\033[1;38;5;{color_256}m'
        return '\n'.join([decorator + line + '\033[0m' for line in cls.LINES])
