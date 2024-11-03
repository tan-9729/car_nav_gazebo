#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped

def pose_callback(msg):
    # 从消息中提取位置坐标
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    z = msg.pose.pose.position.z
    rospy.loginfo("当前坐标: x = %f, y = %f, z = %f", x, y, z)

def main():
    # 初始化 ROS 节点
    rospy.init_node('get_current_position', anonymous=True)

    # 订阅 AMCL 位姿主题
    rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, pose_callback)

    # 循环保持节点活跃
    rospy.spin()

if __name__ == '__main__':
    main()

