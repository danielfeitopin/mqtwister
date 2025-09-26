#!/bin/sh

# Install Mosquitto MQTT clients
apk update
apk add mosquitto-clients

# Add tcpdump for network monitoring
apk add tcpdump

# Copy the subscriber script to the appropriate location
mkdir -p /vagrant/files
cp /tmp/subscribe.sh /vagrant/files/subscribe.sh
chmod +x /vagrant/files/subscribe.sh

# Start the subscriber script in the background
nohup /vagrant/files/subscribe.sh > /dev/null 2>&1 &