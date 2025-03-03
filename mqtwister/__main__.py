from . import context
from .config import TARGET_IP
from .cli.banner import Banner
from .utils.logging import logger
from .utils.network import get_arp_table, get_mac_address

# Display banner
print(Banner.get_colorful_banner(Banner.DEFAULT_COLOR))
print('=' * Banner.WIDTH)

# Get ARP table
logger.info("Getting ARP table...")
context['ARP_TABLE'] = get_arp_table()
logger.debug(f"ARP table: {context['ARP_TABLE']}")

# Get own MAC address
context['OWN_MAC_ADDRESS'] = get_mac_address()
print(f"Own MAC address: {context['OWN_MAC_ADDRESS']}")

# Get target MAC address
context['TARGET_MAC_ADDRESS'] = context['ARP_TABLE'].get(TARGET_IP)
if context.get('TARGET_MAC_ADDRESS') is None:
    print(f"Target's MAC not found!")
    exit(1)
print(f"Target MAC address: {context['TARGET_MAC_ADDRESS']}")
