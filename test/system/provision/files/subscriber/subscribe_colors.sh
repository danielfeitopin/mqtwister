#! /bin/bash
# SPDX-FileCopyrightText: 2026 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

# Load configuration
config_file="/vagrant/subscribe_colors.conf"
if [ -f $config_file ]; then
    source $config_file
else
    echo "Configuration file '$config_file' not found!"
    exit 1
fi

while true; do
    mosquitto_sub -h "$BROKER_IP" -t "colors" | while read line; do
        echo "$(date): $line"
    done
done
