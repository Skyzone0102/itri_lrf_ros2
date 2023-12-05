import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Range
from . import Lrf

# Port
PORT = "/dev/bus/usb/001/014"


class Lrf_Laser(Node):
    def __init__(self):
        super().__init__("Lrf_Laser")
        self.publisher_ = self.create_publisher(Range, "Range", 10)
        # camera connection
        self.com = Lrf.SerialInterface(PORT)
        self.laser = Lrf.Laser(self.com)
        # set camera settings
        self.laser.laserOn()
        # integration time
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Range()
        msg.header.frame_id = "Lrf"
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.radiation_type = Range.INFRARED
        msg.field_of_view = 0.00  # 0.0349065850399 = 2 degrees
        msg.min_range = 0.05
        msg.max_range = 10.0
        msg.range = self.laser.getDistance() / 1000
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    publisher = Lrf_Laser()
    rclpy.spin(publisher)
    publisher.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
