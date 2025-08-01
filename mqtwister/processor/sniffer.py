# SPDX-FileCopyrightText: 2025 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

from mqtwister.config import MQTT_PORT
from mqtwister.cli.messages import get_message as m
from mqtwister.utils.logging import logger
from scapy.all import Packet, AsyncSniffer
from typing import Callable


def get_sniffer(context: dict, prn: Callable = None) -> AsyncSniffer:

    def __prn_wrapper(packet: Packet, context: dict) -> None:
        """Wrapper function to process packets with context."""
        prn(packet, context)

    ifname: str | None = context.get('ifname')
    lmac: str | None = context.get('lmac')
    lport: int | None = context.get('lport', MQTT_PORT)
    logger.info(m('info_starting_sniffer', ifname, lmac, lport))

    filter: str = f"tcp port {context.get('lport', lport)}"
    return AsyncSniffer(iface=ifname, prn=__prn_wrapper, filter=filter, store=0)
