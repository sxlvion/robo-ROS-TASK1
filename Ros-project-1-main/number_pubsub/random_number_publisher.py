import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class RandomNumberPublisher(Node):
    def __init__(self):
        super().__init__('random_number_publisher')
        self.publisher_ = self.create_publisher(Int32, 'numbers', 10)
        self.timer = self.create_timer(1.0, self.publish_number)
        self.get_logger().info("Publisher started...")

    def publish_number(self):
        number = random.randint(1, 100)
        msg = Int32()
        msg.data = number
        self.publisher_.publish(msg)
        self.get_logger().info(f"Published: {number}")

def main(args=None):
    rclpy.init(args=args)
    node = RandomNumberPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

