import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class Ping(Node):
    def __init__(self):
        super().__init__('Ping')
        self.ping = self.create_subscription(
                String,
                'topic',
                self.listener_callback,
                10)
        self.ping

    def listener_callback(self, msg):
        self.get_logger().info("I heard: %s, so I say Ping" % msg.data)


def main(args=None):
    rclpy.init(args=args)

    ping = Ping()

    rclpy.spin(ping)

    ping.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
