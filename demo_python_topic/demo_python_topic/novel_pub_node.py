import rclpy
from rclpy import Node

class novel_pub_node(Node):
    def __init__(self, node_name ):
        super.__init__(node_name)
        self.get_logger().info(f"{node_name},启动!")

def main():
    rclpy.init()
    node = novel_pub_node('novel_pub')
    rclpy.spin(node)
    rclpy.shutdown()
    