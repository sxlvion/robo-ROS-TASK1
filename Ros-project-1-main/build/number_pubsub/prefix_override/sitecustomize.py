import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/parthip/ros2_ws/src/number_pubsub/install/number_pubsub'
