# SPDX-FileCopyrightText: 2025 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

import ipaddress
import platform
import psutil
import re
import subprocess
import uuid
from mqtwister.lang import get_message as m
from mqtwister.utils.logging import logger

IP_MAC_REGEX: re.Pattern = re.compile(
    r"(\d{1,3}(?:\.\d{1,3}){3})"   # IP Address
    + r".*?"  # Intermediate characters
    + r"([\da-fA-F]{2}(?:(?::|[\-])[\da-fA-F]{2}){5})"  # MAC Address
)


def get_mac_address() -> str:
    MAC_CHARS: int = 12  # Number of characters in a MAC address
    mac: int = uuid.getnode()  # 48-bit integer
    mac: str = hex(mac)[2:].zfill(MAC_CHARS)  # Hex string without '0x' prefix
    mac: str = ':'.join([mac[i:i+2] for i in range(0, len(mac), 2)])  # Format
    return mac


def format_mac_address(mac: str) -> str:
    return mac.lower().replace('-', ':')


def get_arp_table() -> dict[str, str]:

    try:

        # Determine the appropriate command based on the OS
        system: str = platform.system().lower()

        if system == 'linux':
            command: list[str] = ["ip", "neigh"]
        elif system == 'windows':
            command: list[str] = ["arp", "-a"]
        else:
            raise NotImplementedError(
                m('error_arp_table_retrieval_not_implemented')
            )

        # Initialize empty dictionary for ARP table
        arp_table: dict[str, str] = {}

        # Execute the command and parse its output
        output: str = subprocess.check_output(command, text=True)
        for line in output.splitlines():
            if match := IP_MAC_REGEX.search(line):
                ip, mac = match.groups()
                arp_table[ip] = format_mac_address(mac)

    except Exception as e:
        logger.error(m('error_retrieving_arp_table', e))

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
