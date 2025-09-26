#!/bin/sh

# Install Mosquitto MQTT broker
apk update
apk add mosquitto

# Add tcpdump for network monitoring
apk add tcpdump

# Replace default config
mkdir -p /etc/mosquitto
cp /tmp/mosquitto.conf /etc/mosquitto/mosquitto.conf

# Enable and start Mosquitto with custom config
rc-update add mosquitto default
rc-service mosquitto restart
