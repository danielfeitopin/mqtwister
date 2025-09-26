#!/bin/bash

BROKER_IP="192.168.56.10"

while true; do
    mosquitto_sub -h "$BROKER_IP" -t "colors" | while read line; do
        echo "$(date): $line" >> /vagrant/files/colors.log
    done
done