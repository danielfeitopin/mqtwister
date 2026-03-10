#! /bin/bash
# SPDX-FileCopyrightText: 2026 Daniel Feito-Pin <danielfeitopin+github@protonmail.com>
#
# SPDX-License-Identifier: GPL-2.0-only

BROKER_IP="" # REPLACE

mosquitto_pub -h $BROKER_IP -t "test/set" -m "Hello, World!"
mosquitto_pub -h $BROKER_IP -t "test/lowercase" -m "Hello, World!"
mosquitto_pub -h $BROKER_IP -t "test/uppercase" -m "Hello, World!"
mosquitto_pub -h $BROKER_IP -t "test/replace" -m "Hello, World!"
mosquitto_pub -h $BROKER_IP -t "test/swap" -m "Hello, World!"
mosquitto_pub -h $BROKER_IP -t "test/prepend" -m "Hello, World!"
mosquitto_pub -h $BROKER_IP -t "test/append" -m "Hello, World!"
mosquitto_pub -h $BROKER_IP -t "test/trim" -m " Hello, World! "
mosquitto_pub -h $BROKER_IP -t "test/truncate" -m "Hello, World!"
mosquitto_pub -h $BROKER_IP -t "test/to_int_str" -m "3.14"
mosquitto_pub -h $BROKER_IP -t "test/to_float_str" -m "3"
mosquitto_pub -h $BROKER_IP -t "test/to_base64" -m "Hello, World!"
mosquitto_pub -h $BROKER_IP -t "test/from_base64" -m "SGVsbG8sIFdvcmxkIQ=="