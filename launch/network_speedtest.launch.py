# SPDX-FileCopyrightText: 2024 Tomoya Tsuji
# SPDX-License-Identifier: Apache-2.0

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    network_speed_measurement = launch_ros.actions.Node(
        package='mypkg',
        executable='network_speed_measurement',
        )
    network_speed_receive = launch_ros.actions.Node(
        package='mypkg',
        executable='network_speed_receive',
        output='screen'
        )

    return launch.LaunchDescription([network_speed_measurement, network_speed_receive])
