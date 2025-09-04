import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EvenOddSubscriber(Node):
    def __init__(self):
        super().__init__('even_odd_subscriber')
        self.subscriber = self.create_subscription(
            Int32, 'numbers', self.listener_callback, 10)
        self.get_logger().info("Subscriber started...")

    def listener_callback(self, msg):
        number = msg.data
        result = "EVEN" if number % 2 == 0 else "ODD"
        self.get_logger().info(f"Received {number} -> {result}")

def main(args=None):
    rclpy.init(args=args)
    node = EvenOddSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

