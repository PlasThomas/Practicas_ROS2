import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/robousr/Documents/Practicas_ROS2/ros2_ws/install/examples_rclpy_minimal_service'
