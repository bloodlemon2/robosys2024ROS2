import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from person_msgs.msg import Person   #通信の型（16ビットの符号付き整数）

rclpy.init()
node = Node("talker")            #ノード作成（nodeという「オブジェクト」を作成）
pub = node.create_publisher(Person, "person", 10)   #パブリッシャのオブジェクト作成
n = 0 #カウント用変数


def cb():          #20行目で定期実行されるコールバック関数
    global n       #関数を抜けてもnがリセットされないようにしている
    msg = Person()  #メッセージの「オブジェクト」
    msg.name = "辻智也"   #msgオブジェクトの持つdataにnを結び付け
    msg.age = n
    pub.publish(msg)        #pubの持つpublishでメッセージ送信
    n += 1


def main():
    node.create_timer(0.5, cb)  #タイマー設定
    rclpy.spin(node)            #実行（無限ループ）
