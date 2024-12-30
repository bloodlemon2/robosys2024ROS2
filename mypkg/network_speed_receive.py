import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class NetworkSpeedReceive(Node):
    def __init__(self):
        super().__init__("network_speed_receive")
        self.download_sub = self.create_subscription(Float32, "download_speed", self.download_cb, 10)
        self.upload_sub = self.create_subscription(Float32, "upload_speed", self.upload_cb, 10)
        self.ping_sub = self.create_subscription(Float32, "ping", self.ping_cb, 10)

    def download_cb(self, msg):
        self.get_logger().info(f'Received download speed: {msg.data:.2f} Mbps')

    def upload_cb(self, msg):
        self.get_logger().info(f'Received upload speed: {msg.data:.2f} Mbps')

    def ping_cb(self, msg):
        self.get_logger().info(f'Received ping: {msg.data:.2f} ms')

def main():
    rclpy.init()
    node = NetworkSpeedReceive()
    rclpy.spin(node)
    rclpy.shutdown()
