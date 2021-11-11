#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64


class AddTenSubscriber(Node):
    def __init__(self):
        super().__init__('addTenSubscriber')
        self.subscriber = self.create_subscription(Float64, 'TenPlus', self.listener_callback, 10)
    
    def listener_callback(self,msg):
        self.get_logger().info("[Subscriber] %f"% msg.data)


def main(args=None):
    rclpy.init(args=args)

    addTenSubscriber = AddTenSubscriber()

    rclpy.spin(addTenSubscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    addTenSubscriber.destroy_node()
    rclpy.shutdown()
