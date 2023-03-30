#!/usr/bin/env python

from geometry_msgs.msg import Twist, Point
import sys
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from math import atan2, pow, sqrt

class TurtleBot:
    def __init__(self):
        rospy.init_node('turtlebot_controller', anonymous=True)
        rospy.Subscriber('/odom', Odometry, self.odom_callback)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.rate = rospy.Rate(10)
        self.position = {'x': 0.0, 'y': 0.0, 'z': 0.0}
        self.orientation = {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 0.0}

    def odom_callback(self, msg):
        self.position['x'] = msg.pose.pose.position.x
        self.position['y'] = msg.pose.pose.position.y
        self.position['z'] = msg.pose.pose.position.z
        self.orientation['x'] = msg.pose.pose.orientation.x
        self.orientation['y'] = msg.pose.pose.orientation.y
        self.orientation['z'] = msg.pose.pose.orientation.z
        self.orientation['w'] = msg.pose.pose.orientation.w

    def move_to_goal(self, x_goal, y_goal):
        goal = Point()
        goal.x = x_goal
        goal.y = y_goal
        distance_tolerance = 0.1
        vel_msg = Twist()
        while sqrt(pow((goal.x - self.position['x']), 2) + pow((goal.y - self.position['y']), 2)) >= distance_tolerance:
            # Calculate the angle to the goal
            angle_to_goal = atan2(goal.y - self.position['y'], goal.x - self.position['x'])

            # Turn towards the goal
            if angle_to_goal - self.orientation['z'] > 0.1:
                vel_msg.angular.z = 0.5
            elif angle_to_goal - self.orientation['z'] < -0.1:
                vel_msg.angular.z = -0.5
            else:
                vel_msg.angular.z = 0

            # Move towards the goal
            vel_msg.linear.x = 0.5
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            self.pub.publish(vel_msg)
            self.rate.sleep()

        # Stop the robot when the goal is reached
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.pub.publish(vel_msg)
        rospy.spin()

if __name__ == '__main__':
    try:
        x_goal = float(sys.argv[1])
        y_goal = float(sys.argv[2])
    except:
        print("Please enter x and y coordinates for the goal.")
        sys.exit()

    tb = TurtleBot()
    tb.move_to_goal(x_goal, y_goal)
