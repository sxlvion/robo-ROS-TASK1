import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class EvenOddSubscriber(Node):
    def __init__(self):
        super().__init__('even_odd_subscriber')
        self.subscription = self.create_subscription(
            Int32,
            'numbers',
            self.listener_callback,
            10
        )
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        number = msg.data
        if number % 2 == 0:
            self.get_logger().info(f'Received: {number} → Even')
        else:
            self.get_logger().info(f'Received: {number} → Odd')


def main(args=None):
    rclpy.init(args=args)
    node = EvenOddSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
