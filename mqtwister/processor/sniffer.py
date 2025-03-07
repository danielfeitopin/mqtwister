from scapy.all import AsyncSniffer


def get_sniffer(iface: str, prn: 'function' = None) -> AsyncSniffer:
    FILTER: str = "tcp port 1883"
    return AsyncSniffer(iface=iface, prn=prn, filter=FILTER, store=0)
