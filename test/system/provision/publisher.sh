#! /bin/bash
# SPDX-FileCopyrightText: 2026 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

# === Install software ===

apk update

# Install Mosquitto MQTT clients
apk add mosquitto-clients

# Add tcpdump for network monitoring
apk add tcpdump

# === Set up preferences ===

# Set up bash profile for vagrant user and root
install -o vagrant -g vagrant -m 600 -t /home/vagrant /tmp/provision_files/.bash_profile
install -o root -g root -m 600 -t /root /tmp/provision_files/.bash_profile

# === Set up service ===

# Copy the script to the appropriate location
install -m 755 -Dt /vagrant /tmp/provision_files/publish_colors.sh

# Copy the service script to the init.d directory
install -m 755 -D /tmp/provision_files/publish_colors_service.sh /etc/init.d/publish_colors

# Save the script configuration
echo "BROKER_IP=${BROKER_IP}" > /vagrant/publish_colors.conf
echo "INTERVAL=2" >> /vagrant/publish_colors.conf

# Enable the service to start on boot
rc-update add publish_colors default

# Start the publisher service
rc-service publish_colors restart

# === Clean up ===

# Remove the provisioning files
rm -rf /tmp/provision_files
