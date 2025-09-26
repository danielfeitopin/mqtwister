#!/bin/bash

BROKER_IP="192.168.56.10"
COLORS=("GREEN" "YELLOW" "RED")

while true; do
    for color in "${COLORS[@]}"; do
        mosquitto_pub -h "$BROKER_IP" -t "colors" -m "$color"
        sleep 2
    done
done
