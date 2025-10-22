#!/bin/sh

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
install -Dt /etc/mosquitto /tmp/provision_files/mosquitto.conf

# Enable the service to start on boot
rc-update add mosquitto default

# Start the publisher service
rc-service mosquitto restart

# === Clean up ===

# Remove the provisioning files
rm -rf /tmp/provision_files
