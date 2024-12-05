import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from std_msgs.msg import Int16   #通信の型（16ビットの符号付き整数）


class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        self.pub = self.create_publisher(Int16, "countup", 10)
        self.n = 0
        self.create_timer(0.5, self.cb)

    def cb(self):          #20行目で定期実行されるコールバック関数
        msg = Int16()  #メッセージの「オブジェクト」
        msg.data = self.n   #msgオブジェクトの持つdataにnを結び付け
        self.pub.publish(msg)        #pubの持つpublishでメッセージ送信
        self.n += 1


def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)            #実行（無限ループ）
