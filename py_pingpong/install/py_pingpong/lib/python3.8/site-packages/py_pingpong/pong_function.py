import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class Pong(Node):

    def __init__(self):
        super().__init__('pong')
        self.pong = self.create_publisher(String, "topic", 10)
        timer_period = 1 #seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = "Pong (call #%d)" % self.i
        self.pong.publish(msg)
        self.get_logger().info("Publishing: '%s'" % msg.data)
        self.i += 1
    

def main(args=None):
        rclpy.init(args=args)

        pong = Pong()

        rclpy.spin(pong)

        pong.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
