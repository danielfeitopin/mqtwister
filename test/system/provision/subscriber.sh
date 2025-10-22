#!/bin/sh

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
install -m 755 -Dt /vagrant /tmp/provision_files/subscribe_colors.sh

# Copy the service script to the init.d directory
install -m 755 -D /tmp/provision_files/subscribe_colors_service.sh /etc/init.d/subscribe_colors

# Save the script configuration
echo "BROKER_IP=${BROKER_IP}" > /vagrant/subscribe_colors.conf

# Enable the service to start on boot
rc-update add subscribe_colors default

# Start the subscriber service
rc-service subscribe_colors restart

# === Clean up ===

# Remove the provisioning files
rm -rf /tmp/provision_files
