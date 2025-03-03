from . import context
from .config import TARGET_IP, INTERFACE_NAME
from .cli.banner import Banner
from .utils.logging import logger
from .utils.network import get_arp_table, get_interface_mac
import sys

# Display banner
print(Banner.get_colorful_banner(Banner.DEFAULT_COLOR))
print('=' * Banner.WIDTH)

# Get ARP table
logger.info("Getting ARP table...")
context['ARP_TABLE'] = get_arp_table()
logger.debug(f"ARP table: {context['ARP_TABLE']}")

# Get own MAC address
context['OWN_MAC_ADDRESS'] = get_interface_mac(INTERFACE_NAME)
if not context.get('OWN_MAC_ADDRESS'):
    msg = f"MAC address not found for interface '{INTERFACE_NAME}'"
    logger.error(msg)
    print(msg)
    sys.exit(1)
print(f"Own MAC address: {context['OWN_MAC_ADDRESS']}")

# Get target MAC address
context['TARGET_MAC_ADDRESS'] = context['ARP_TABLE'].get(TARGET_IP)
if not context.get('TARGET_MAC_ADDRESS'):
    msg = f"Target's MAC not found!"
    logger.error(msg)
    print(msg)
    sys.exit(1)
print(f"Target MAC address: {context['TARGET_MAC_ADDRESS']}")
