import rclpy
from rclpy import Node

class novel_pub_node(Node):
    def __init__(self, node_name ):
        super.__init__(node_name)
        self.get_logger().info(f"{node_name},启动!")  #节点启动标识（实际可写可不写）

def main():
    rclpy.init()
    node = novel_pub_node('自己取个名字')
    rclpy.spin(node)
    rclpy.shutdown()
    