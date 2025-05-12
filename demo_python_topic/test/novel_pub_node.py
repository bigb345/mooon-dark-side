import rclpy
import requests
from rclpy import Node

class novel_pub_node(Node):
    def __init__(self, node_name ):
        super.__init__(node_name)
        self.get_logger().info(f"{node_name},启动!")

    def download(self,url):
        response = requests.get(url)
        response.encoding = 'utf-8'

def main():
    rclpy.init()
    node = novel_pub_node('novel_pub')
    node.download('http://0.0.0.0:8000/aiyuetv.txt')
    rclpy.spin(node)
    rclpy.shutdown()
    