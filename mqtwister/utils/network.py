# SPDX-FileCopyrightText: 2025 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

import ipaddress
import psutil
import re
import subprocess
import uuid


def get_mac_address() -> str:
    MAC_CHARS: int = 12  # Number of characters in a MAC address
    mac: int = uuid.getnode()  # 48-bit integer
    mac: str = hex(mac)[2:].zfill(MAC_CHARS)  # Hex string without '0x' prefix
    mac: str = ':'.join([mac[i:i+2] for i in range(0, len(mac), 2)])  # Format
    return mac


def format_mac_address(mac: str) -> str:
    return mac.lower().replace('-', ':')


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
                arp_table[ip] = format_mac_address(mac)
    except Exception as e:
        print(f"Error reading ARP table: {e}")

    # Sort the ARP table by IP address
    arp_table = dict(sorted(arp_table.items(),
                            key=lambda item: ipaddress.ip_address(item[0])))

    return arp_table


def get_interfaces() -> list[str]:
    return list(psutil.net_if_addrs().keys())


def get_interface_mac(interface_name: str) -> str | None:
    mac: str | None = None
    interfaces = psutil.net_if_addrs()
    if interface_name in interfaces:
        for snicaddr in interfaces[interface_name]:
            if snicaddr.family == psutil.AF_LINK:
                mac: str = format_mac_address(snicaddr.address)
                break
    return mac


def validate_mac_address(mac: str) -> bool:
    """Validate a MAC address format."""

    mac_regex: str = r'^([0-9a-fA-F]{2}[:-]){5}([0-9a-fA-F]{2})$'
    return bool(re.match(mac_regex, mac))
