#!/usr/bin/env python
import rospy, random
from std_msgs.msg import Float64

rospy.init_node('simple_pub')
pub = rospy.Publisher('uniform_rand', Float64, queue_size=10)
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    r = Float64()
    r.data = random.uniform(0.0,1.0)
    pub.publish(r)
    rate.sleep()
