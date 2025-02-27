import re
import subprocess


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
                ip, mac = match.groups()
                arp_table[ip] = mac
    except Exception as e:
        print(f"Error reading ARP table: {e}")
    return arp_table