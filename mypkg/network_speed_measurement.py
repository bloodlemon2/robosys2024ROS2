# SPDX-FileCopyrightText: 2024 Tomoya Tsuji
# SPDX-License-Identifier: Apache-2.0

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import speedtest


class NetworkSpeedMeasurement(Node):
    def __init__(self):
        super().__init__("network_speed_measurement")
        self.download_pub = self.create_publisher(Float32, 'download_speed', 10)
        self.upload_pub = self.create_publisher(Float32, 'upload_speed', 10)
        self.ping_pub = self.create_publisher(Float32, 'ping', 10)
        self.timer = self.create_timer(60.0, self.cb)


    def cb(self):
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Mbps
        upload_speed = st.upload() / 1_000_000  # Mbps
        ping = st.results.ping #ms
            
        # ダウンロード速度を送信
        download_msg = Float32()
        download_msg.data = download_speed
        self.download_pub.publish(download_msg)

        # アップロード速度を送信
        upload_msg = Float32()
        upload_msg.data = upload_speed
        self.upload_pub.publish(upload_msg)

        # pingを送信
        ping_msg = Float32()
        ping_msg.data = ping
        self.ping_pub.publish(ping_msg)

def main():
    rclpy.init()
    node = NetworkSpeedMeasurement()
    rclpy.spin(node)
    rclpy.shutdown()
