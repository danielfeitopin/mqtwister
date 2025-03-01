from . import context
from .config import TARGET_IP
from .menu import Banner
from .utils import get_arp_table, get_mac_address

# Display banner
print(Banner.get_colorful_banner(214))
print('=' * Banner.WIDTH)

# Get ARP table
print("Getting ARP table...", end=" ")
context['ARP_TABLE'] = get_arp_table()
print("Done!")

# Get own MAC address
context['OWN_MAC_ADDRESS'] = get_mac_address()
print(f"Own MAC address: {context['OWN_MAC_ADDRESS']}")

# Get target MAC address
context['TARGET_MAC_ADDRESS'] = context['ARP_TABLE'].get(TARGET_IP)
if context.get('TARGET_MAC_ADDRESS') is None:
    print(f"Target's MAC not found!")
    exit(1)
print(f"Target MAC address: {context['TARGET_MAC_ADDRESS']}")
