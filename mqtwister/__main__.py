# SPDX-FileCopyrightText: 2025 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only


def main(context: dict = {}) -> None:
    """Main function to run the MQTwister CLI."""

    # Display banner
    from .cli.banner import Banner
    print(Banner.get_colorful_banner(Banner.DEFAULT_COLOR))

    # Retrieve and set context values
    from .config import TARGET_IP, INTERFACE_NAME, MQTT_PORT
    context['ifname'] = INTERFACE_NAME
    # context['lmac'] = get_interface_mac(INTERFACE_NAME)

    # Show the main menu
    from .cli.menu import show_menu
    while True:
        show_menu(context)
        print()

    # Start sniffer
    # msg = "Starting sniffer..."
    # logger.info(msg)
    # print(msg)
    # sniffer = get_sniffer(INTERFACE_NAME, packet_callback, MQTT_PORT)

    #     sniffer.start()

    #     if sniffer.exception:
    #         raise sniffer.exception

    #     # Wait for user to stop the sniffer
    #     input("Press ENTER to stop the sniffer...\n")
    #     msg = "Stopping sniffer..."
    #     logger.info(msg)
    #     if sniffer.running:
    #         sniffer.stop()
    #     logger.info("Sniffer stopped.")
    #     sys.exit(0)


if __name__ == "__main__":

    import sys
    from .cli.messages import get_message as m
    from .utils.logging import logger

    try:
        main()

    except KeyboardInterrupt:
        sys.exit(0)

    except PermissionError:
        logger.error(m('error_permission_denied'))
        sys.exit(1)
