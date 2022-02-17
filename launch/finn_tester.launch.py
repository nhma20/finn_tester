import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    finn_interfacer = Node(
        package="finn-example",
        executable="finn_interfacer",
        name="finn_interfacer",
        namespace="finn_interfacer",
        remappings=[("/image", "/test_image")]
    )

    finn_tester = Node(
        package="finn_tester",
        executable="finn_tester",
        name="finn_tester",
        namespace="finn_tester",
    )

    return LaunchDescription([
        finn_interfacer,
        finn_tester
    ])
