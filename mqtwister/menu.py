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
    COLOR: int = 202

    @classmethod
    def get_banner(cls) -> str:
        return f'\033[1m' + cls.TEXT + '\033[0m'

    @classmethod
    def get_colorful_banner(cls, color_256: int = COLOR) -> str:
        return f'\033[1;38;5;{color_256}m' + cls.TEXT + '\033[0m'
