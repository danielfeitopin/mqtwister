# SPDX-FileCopyrightText: 2025 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

from mqtwister.cli import BANNER_WIDTH

class Banner:

    LINES: list[str] = [
        r" __  __  ___ _____          _    _____         ".center(BANNER_WIDTH),
        r"|  \/  |/ _ \_   _|_      _(_)__|_   _|__ _ __ ".center(BANNER_WIDTH),
        r"| |\/| | | | || | \ \ /\ / / / __|| |/ _ \ '__|".center(BANNER_WIDTH),
        r"| |  | | |_| || |  \ V  V /| \__ \| |  __/ |   ".center(BANNER_WIDTH),
        r"|_|  |_|\__\_\|_|   \_/\_/ |_|___/|_|\___|_|   ".center(BANNER_WIDTH),
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
