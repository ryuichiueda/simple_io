#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

def cb(message):
    rospy.loginfo("received: %f", message.data)

rospy.init_node('sub')
sub = rospy.Subscriber('uniform_rand', Float64, cb)
rospy.spin()
