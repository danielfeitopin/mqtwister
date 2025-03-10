import sys
from . import context
from .config import TARGET_IP, INTERFACE_NAME, MQTT_PORT
from .cli.banner import Banner
from .processor.sniffer import get_sniffer
from .processor.mqtt import packet_callback
from .utils.logging import logger
from .utils.network import get_arp_table, get_interface_mac

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

# Start sniffer
msg = "Starting sniffer..."
logger.info(msg)
print(msg)
sniffer = get_sniffer(INTERFACE_NAME, packet_callback, MQTT_PORT)

try:
    sniffer.start()
    
    if sniffer.exception:
        raise sniffer.exception
    
    # Wait for user to stop the sniffer
    input("Press a key to stop the sniffer...\n")
    msg = "Stopping sniffer..."
    logger.info(msg)
    if sniffer.running:
        sniffer.stop()
    logger.info("Sniffer stopped.")
    sys.exit(0)

except KeyboardInterrupt:
    sys.exit(0)
    
except PermissionError:
    msg = "Permission denied."
    logger.error(msg)
    print(msg, end=" ")
    print("Please run as root.")
    sys.exit(1)
