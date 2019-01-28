#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

value = 0

def callback(msg):
	#obtain the minimun
  value = 0

  for i in range(1,719):
    #print msg.ranges[i]
    if (msg.ranges[i] < 30.0):		#max range is 30m
	if (msg.ranges[i] > value):
		value = msg.ranges[i]

  print value
   
rospy.init_node('scan_values')
sub = rospy.Subscriber(rospy.get_param('scan_subscriber_topic_name'), LaserScan, callback)
rospy.spin()

