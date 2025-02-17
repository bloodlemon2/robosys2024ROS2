from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'ros2_speedtest_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=[
        'setuptools'
        'speedtest-cli',
    ],
    zip_safe=True,
    maintainer='Tomoya Tsuji',
    maintainer_email='s23c1093hj@s.chibakoudai.jp',
    description='ロボットシステム学ROS 2パッケージ',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'network_speed_measurement = ros2_speedtest_pkg.network_speed_measurement:main',
            'network_speed_receive = ros2_speedtest_pkg.network_speed_receive:main',
        ],
    },
)
