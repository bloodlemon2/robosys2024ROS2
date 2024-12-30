#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 120 ros2 launch mypkg network_speedtest.launch.py | tee /tmp/mypkg.log

(cat /tmp/mypkg.log | grep 'Received download speed:') && (cat /tmp/mypkg.log | grep 'Received upload speed:') && (cat /tmp/mypkg.log | grep 'Received ping:')
