#!/bin/sh

# Install Mosquitto MQTT clients
apk update
apk add mosquitto-clients

# Add tcpdump for network monitoring
apk add tcpdump

# Copy the publisher script to the appropriate location
mkdir -p /vagrant/files
cp /tmp/publish.sh /vagrant/files/publish.sh
chmod +x /vagrant/files/publish.sh

# Start the publisher script in the background
nohup /vagrant/files/publish.sh > /dev/null 2>&1 &