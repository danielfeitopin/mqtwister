#! /bin/bash
# SPDX-FileCopyrightText: 2026 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

# === Install software ===

apk update

# Install Mosquitto MQTT broker
apk add mosquitto

# Add tcpdump for network monitoring
apk add tcpdump

# === Set up preferences ===

# Set up bash profile for vagrant user and root
install -o vagrant -g vagrant -m 600 -t /home/vagrant /tmp/provision_files/.bash_profile
install -o root -g root -m 600 -t /root /tmp/provision_files/.bash_profile

# === Set up service ===

# Copy the Mosquitto configuration file
install -o mosquitto -g mosquitto -Dt /etc/mosquitto /tmp/provision_files/mosquitto.conf

# Create log directory if it doesn't exist
if [ -f /var/log/mosquitto.log ]; then
    echo "Log file '/var/log/mosquitto.log' already exists"
else
    install -o mosquitto -g mosquitto -m 640 -D /dev/null /var/log/mosquitto.log
fi

# Enable the service to start on boot
rc-update add mosquitto default

# Start the publisher service
rc-service mosquitto restart

# === Clean up ===

# Remove the provisioning files
rm -rf /tmp/provision_files
