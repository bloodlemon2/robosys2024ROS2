import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    network_speed_measurement = launch_ros.actions.Node(
        package='mypkg',      #パッケージの名前を指定
        executable='network_speed_measurement',  #実行するファイルの指定
        output='screen'
        )
    network_speed_receive = launch_ros.actions.Node(
        package='mypkg',
        executable='network_speed_receive',
        output='screen'    #ログを端末に出すための設定
        )

    return launch.LaunchDescription([network_speed_measurement, network_speed_receive])
