import re
import subprocess
import uuid


def get_arp_table() -> dict[str, str]:
    COMMAND: list[str] = ["arp", "-a"]

    ip_mac_regex: str = r''
    ip_mac_regex += r"(\d{1,3}(?:\.\d{1,3}){3})"  # IP
    ip_mac_regex += r".*?"  # Intermediate characters
    ip_mac_regex += r"([\da-fA-F]{2}(?:(?::|[\-])[\da-fA-F]{2}){5})"  # MAC

    arp_table: dict[str, str] = {}

    try:
        output: str = subprocess.check_output(COMMAND, text=True)
        for line in output.splitlines():
            if match := re.search(ip_mac_regex, line):
                arp_table.update([match.groups()])
    except Exception as e:
        print(f"Error reading ARP table: {e}")
    return arp_table


def get_mac_address() -> str:
    MAC_CHARS: int = 12  # Number of characters in a MAC address
    mac: int = uuid.getnode()  # 48-bit integer
    mac: str = hex(mac)[2:].zfill(MAC_CHARS)  # Hex string without '0x' prefix
    mac: str = ':'.join([mac[i:i+2] for i in range(0, len(mac), 2)])  # Format
    return mac
