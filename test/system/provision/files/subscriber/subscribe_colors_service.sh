#! /sbin/openrc-run
# SPDX-FileCopyrightText: 2026 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

name="subscribe_colors"
description="MQTT Color Subscriber Service"

command="/vagrant/subscribe_colors.sh"
command_background="yes"
output_log="/var/log/${name}.log"
error_log="/var/log/${name}.log"
pidfile="/var/run/${name}.pid"

depend() {
    need net
    after net
}

start_pre() {
    echo "Starting $description..."
}

stop_post() {
    echo "Stopped $description."
}
