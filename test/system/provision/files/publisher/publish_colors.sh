#!/bin/bash

colors=("GREEN" "YELLOW" "RED")

# Load configuration
config_file="/vagrant/publish_colors.conf"
if [ -f $config_file ]; then
    source $config_file
else
    echo "Configuration file '$config_file' not found!"
    exit 1
fi

while true; do
    for color in "${colors[@]}"; do
        mosquitto_pub -h "$BROKER_IP" -t "colors" -m "$color"
        sleep $INTERVAL
    done
done
