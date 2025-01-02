# robosys2024ROS2
ロボットシステム学のROS 2のパッケージ格納用のリポジトリです.
## このパッケージの概要
このパッケージは接続しているネットワークの通信速度を, 60秒ごとに計測して表示させます.  
計測する通信速度は以下のものです.
- ダウンロード
- アップロード
- Ping(通信の応答速度)
## ノード
このパッケージは以下の2つのノードがあります.
- network_speed_measurement
    - このノードは以下の3つのパブリッシャを持ちます.
        - ダウンロードの通信速度をdownload_speedというトピックにパブリッシュします.
        - アップロードの通信速度をupload_speedというトピックにパブリッシュします.
        - Pingをpingというトピックにパブリッシュします.
- network_speed_receive
    - このノードは以下の3つのサブスクライバを持ちます.
        - download_speedというトピックからダウンロードの通信速度をサブスクライブします.
        - upload_speedというトピックからアップロードの通信速度がサブスクライブします.
        - pingというトピックからPingをサブスクライブします.
## 実行例
以下のコマンドで実行できます.
```
ros2 launch mypkg network_speedtest.launch.py
```
```
# 実行後60秒ごとに通信速度の計測を開始
# 計測開始から数十秒待つと通信速度が表示される
[network_speed_receive-2] [INFO] [1735712536.921329873] [network_speed_receive]: Received download speed: 8.53 Mbps
[network_speed_receive-2] [INFO] [1735712536.921769549] [network_speed_receive]: Received upload speed: 10.10 Mbps
[network_speed_receive-2] [INFO] [1735712536.922029270] [network_speed_receive]: Received ping: 62.04 ms
# 2回目の計測結果
[network_speed_receive-2] [INFO] [1735712596.100170886] [network_speed_receive]: Received download speed: 16.51 Mbps
[network_speed_receive-2] [INFO] [1735712596.100694220] [network_speed_receive]: Received upload speed: 10.20 Mbps
[network_speed_receive-2] [INFO] [1735712596.101065018] [network_speed_receive]: Received ping: 31.18 ms
```
## このパッケージを使用する準備
- ROS 2のインストール  
ROS 2のインストールは各自で行ってください.
- speedtest-cliのインストール  
Ubuntu 24.04ではpipでのインストールが難しかったので次の手順でインストールしました.
```
$ sudo apt-get update
$ sudo apt-get install speedtest-cli
```
[speedtest-cli](https://github.com/sivel/speedtest-cli/?tab=readme-ov-file)のGitHubリポジトリをクローンしてインストールすることも可能です.
- このパッケージのインストール
```
# このリポジトリをクローン
# ros2_wsは各自のROS 2のワークスペース名に変更してください
$ cd ~/ros2_ws/src/
$ git clone https://github.com/bloodlemon2/robosys2024ROS2.git

# ビルドしてインストール完了
$ cd ~/ros2_ws/
$ colcon build
$ source ~/ros2_ws/install/setup.bash
$ source ~/ros2_ws/install/local_setup.bash


# 'source ~/ros2_ws/install/setup.bash'と'source ~/ros2_ws/install/local_setup.bash'は, ~/.bashrcに書いておくことを推奨します.   
# 下のコマンドで~/.bashrcに追記できます.  
$ echo 'source ~/ros2_ws/install/setup.bash' >> ~/.bashrc
$ echo 'source ~/ros2_ws/install/local_setup.bash' >> ~/.bashrc
# ~/.bashrcに追記すると下のコマンドが代わりに使用できます.
$ source ~/.bashrc
```
## テスト環境
- ROS 2 Jazzy (Ubuntu 24.04 LTSで, 自身のノートPCでテスト)
- ROS 2 Humble (Ubuntu 22.04 LTSで, GitHub Actionsでテスト)
# ライセンス
- このパッケージはsivelが公開している[speedtest-cli](https://github.com/sivel/speedtest-cli/?tab=readme-ov-file)を利用しています.
    - speedtest-cliはApache License, Version 2.0に基づき公開されています.
- このパッケージはApache License, Version 2.0に基づき公開されています.
- © 2024 Tomoya Tsuji
