# ros2_speedtest_pkg
このパッケージは接続しているネットワークの通信速度を, 60秒ごとに計測して表示させるROS 2のパッケージです.  
計測する通信速度は以下のものです.
- ダウンロード
- アップロード
- Ping（通信の応答速度）
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
## このパッケージを使用する前に
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
このパッケージのインストールは各自で行ってください.
## 実行例
### ros2 runでの実行
- 端末1  
以下のコマンドで実行し, 通信速度の計測をします.
```
$ ros2 run ros2_speedtest_pkg network_speed_measurement
# （何も表示されません）
# 60秒ごとに通信速度の計測を開始
```
- 端末2  
以下のコマンドで実行し, 計測結果を表示します.
```
$ ros2 run ros2_speedtest_pkg network_speed_receive
# 計測開始から数十秒待つと計測結果を受け取り, 表示
[INFO] [1735889869.162479497] [network_speed_receive]: Received download speed: 17.65 Mbps
[INFO] [1735889869.163005184] [network_speed_receive]: Received upload speed: 8.67 Mbps
[INFO] [1735889869.163456932] [network_speed_receive]: Received ping: 35.67 ms
# 2回目の計測結果
[INFO] [1735889930.341374969] [network_speed_receive]: Received download speed: 12.10 Mbps
[INFO] [1735889930.341789744] [network_speed_receive]: Received upload speed: 7.15 Mbps
[INFO] [1735889930.342058465] [network_speed_receive]: Received ping: 37.31 ms
```
### ros2 launchでの実行
以下のコマンドで実行できます.
```
$ ros2 launch ros2_speedtest_pkg network_speedtest.launch.py
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
## テスト環境
- ROS 2 Jazzy（Ubuntu 24.04 LTSで, 自身のノートPCでテスト）
- ROS 2 Humble（Ubuntu 22.04 LTSで, GitHub Actionsでテスト）
# ライセンス
- このパッケージはsivelが公開している[speedtest-cli](https://github.com/sivel/speedtest-cli/?tab=readme-ov-file)を利用しています.
    - speedtest-cliはApache License, Version 2.0に基づき公開されています.
- このパッケージの[test.yml](https://github.com/bloodlemon2/ros2_speedtest_pkg/blob/main/.github/workflows/test.yml)では, [こちらのコンテナ](https://hub.docker.com/r/ryuichiueda/ubuntu22.04-ros2)（by Ryuichi Ueda）を利用しています.
- このパッケージはApache License, Version 2.0に基づき公開されています.
- © 2024 Tomoya Tsuji
