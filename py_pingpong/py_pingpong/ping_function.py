import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class Ping(Node):
    def __init__(self):
        super().__init__('Ping')
        self.ping = self.create_publisher(String, 'topic', 10)
        timer_period = 1 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = "Ping"
        self.ping.publish(msg)
        self.get_logger().info("Publishing '%s'" % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    ping = Ping()

    rclpy.spin(ping)

    ping.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
