# SPDX-FileCopyrightText: 2025 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

from scapy.all import AsyncSniffer


def get_sniffer(iface: str, prn: 'function' = None,
                port: int = 1883) -> AsyncSniffer:
    FILTER: str = f"tcp port {port}"
    return AsyncSniffer(iface=iface, prn=prn, filter=FILTER, store=0)
