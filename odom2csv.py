#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import rospy
from nav_msgs.msg import Odometry
import os

file = "filename.csv"

_odom_x,_odom_y = 0.0,0.0

def csv_callback(msg):
    global _odom_x,_odom_y
    _odom_x = msg.pose.pose.position.x
    _odom_y = msg.pose.pose.position.y

    buf = str(_odom_x) + "," + str(_odom_y) + "\n"
    with open(file, mode = 'a') as f:
        f.write(buf)
        rospy.loginfo("odom_x : %s odom_y : %s",_odom_x,_odom_y)



def odometry2csv():
    rospy.init_node('odom2csv')
    odom_sub = rospy.Subscriber('/odom', Odometry, csv_callback)

    rospy.spin()

if __name__=='__main__':
    odometry2csv()