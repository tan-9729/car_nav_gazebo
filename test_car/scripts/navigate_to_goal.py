#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy

def get_goal_coordinates():
    # 初始化 ROS 节点
    rospy.init_node('get_goal_coordinates', anonymous=True)

    try:
        # 获取用户输入的目标点坐标
        x = float(input("请输入目标点的 x 坐标: "))
        y = float(input("请输入目标点的 y 坐标: "))

        # 输出目标点坐标
        rospy.loginfo("目标点坐标: x = %f, y = %f", x, y)

    except ValueError:
        rospy.logerr("输入无效，请输入数字。")

if __name__ == '__main__':
    get_goal_coordinates()


