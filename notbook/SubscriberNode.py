#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# ROS2 Python接口库
# ROS2 节点类
# 字符串消息类型

class SubscriberNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.sub = self.create_subscription(String, "chatter", self.listener_callback, 10)
        # ROS2节点初始化
        # 创建订阅者对象（消息类型，话题名，订阅回调函数，队列长度）
        # 创建一个订阅器（用处类，话题名，订阅回调函数，队列长度）

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        # 创建回调函数，执行订阅话题后对数据的数据处理
        # 输出日志信息，提示已经收到订阅的的消息

def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode("topic_helloworld_sub")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    # ROS2节点主入口main函数
    # ROS2 Python接口初始化
    # 创建ROS2节点对象并运行初始化
    # 循环ROS2事件
    # 销毁节点对象
    # 关闭ROS2 Python接口