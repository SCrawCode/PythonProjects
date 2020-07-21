#!/usr/bin/env python

import rospy

if __name__ == '__main__':
	rospy.init_node('first_python_node')
	rospy.loginfo("This node has started")

	rate = rospy.Rate(10)
	
	while not rospy.is_shutdown():	#While node is not shutdown, continue program
		rospy.loginfo("Henlo")
		rate.sleep()		#Sleep for every 0.1 sec (10 Hz)
