#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64
from add_ten_srv.srv import AddTen


class AddTenPublisher(Node):

    def __init__(self):
        super().__init__('addTenPublisher')
        self.publisher = self.create_publisher(Float64, 'TenPlus', 1)
        self.currentNumber = 0
        self.srv = self.create_service(AddTen, 'add_ten', self.add_ten_callback)
        self.timer = self.create_timer(0.5, self.timer_callback)
    
    def timer_callback(self):
        msg = Float64()
        msg.data = float(self.currentNumber)
        self.publisher.publish(msg)
        self.get_logger().info("[Publisher] %f"% msg.data)

    def add_ten_callback(self, req, res):
        self.currentNumber = req.before + float(10)
        res.after = self.currentNumber 
        return res 



def main(args=None):
    rclpy.init(args=args)

    addTenPublisher = AddTenPublisher()

    rclpy.spin(addTenPublisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    addTenPublisher.destroy_node()
    rclpy.shutdown()
