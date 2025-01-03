#!/bin/bash
# SPDX-FileCopyrightText: 2024 Tomoya Tsuji
# SPDX-License-Identifier: Apache-2.0

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 120 ros2 launch ros2_speedtest_pkg network_speedtest.launch.py | tee /tmp/mypkg.log

(cat /tmp/mypkg.log | grep 'Received download speed:') && (cat /tmp/mypkg.log | grep 'Received upload speed:') && (cat /tmp/mypkg.log | grep 'Received ping:')
