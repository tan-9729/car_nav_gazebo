#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped
from actionlib_msgs.msg import GoalStatusArray

# 更新后的目标点坐标列表
waypoints = [
    (-5.884349, -1.208057),  # 第一个点
    (-0.575750, -1.107178),   # 第二个点
    (-5.587783, 2.001139)     # 第三个点
]

class Navigator:
    def __init__(self):
        rospy.init_node('navigate_to_three_points', anonymous=True)
        self.goal_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
        self.status_sub = rospy.Subscriber('/move_base/status', GoalStatusArray, self.status_callback)

        self.current_goal_index = 0
        self.reached_goal = False

    def status_callback(self, msg):
        if msg.status_list:
            status = msg.status_list[-1].status
            rospy.loginfo("当前状态: %d", status)  # 调试信息
            if status == 3:  # 目标已成功完成
                self.reached_goal = True

    def navigate_to_goal(self, x, y):
        goal = PoseStamped()
        goal.header.frame_id = "map"
        goal.header.stamp = rospy.Time.now()
        
        goal.pose.position.x = x
        goal.pose.position.y = y
        goal.pose.position.z = 0.0
        
        goal.pose.orientation.x = 0.0
        goal.pose.orientation.y = 0.0
        goal.pose.orientation.z = 0.0
        goal.pose.orientation.w = 1.0
        
        self.goal_pub.publish(goal)
        rospy.loginfo("导航到目标点: [%f, %f]", x, y)

    def run(self):
        rospy.sleep(1)  # 等待初始化
        while self.current_goal_index < len(waypoints):
            x, y = waypoints[self.current_goal_index]
            self.reached_goal = False  # 重置到达标志
            self.navigate_to_goal(x, y)

            # 等待目标到达
            timeout = rospy.Time.now() + rospy.Duration(30)  # 设置一个超时
            while not rospy.is_shutdown() and not self.reached_goal:
                if rospy.Time.now() > timeout:
                    rospy.logwarn("到达目标超时，正在跳过目标点: [%f, %f]", x, y)
                    break  # 超时，跳过目标点
                rospy.sleep(0.5)

            if self.reached_goal:
                rospy.loginfo("到达目标点: [%f, %f]", x, y)
                self.current_goal_index += 1  # 目标成功，前往下一个点
            else:
                rospy.loginfo("未到达目标点: [%f, %f]", x, y)

        rospy.loginfo("所有目标点已处理完成。")

if __name__ == '__main__':
    try:
        navigator = Navigator()
        navigator.run()
    except rospy.ROSInterruptException:
        pass

