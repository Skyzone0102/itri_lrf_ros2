import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range
from . import Lrf


class EdgeWarning(Node):
    def __init__(self):
        super().__init__("edge_warning")
        self.subscription = self.create_subscription(
            Range, "Range", self.edgeDetection, 10
        )
        self.subscription  # prevent unused variable warning
        self.last_range = 0.0

    def edgeDetection(self, msg):
        if self.last_range - msg.range > 0.5 or self.last_range - msg.range < -0.5:
            self.get_logger().info("Edge Warning '%s'" % msg.range)
        self.last_range = msg.range

    # def listener_callback(self, msg):

    #     self.get_logger().info("Publishing: '%s'" % msg.range)


def main(args=None):
    rclpy.init(args=args)
    subscriber = EdgeWarning()
    rclpy.spin(subscriber)
    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
