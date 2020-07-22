#!/usr/bin/env python

#Simple publisher node source code that transmits topic (Robot News Radio) to subscribers

import rospy
from std_msgs.msg import String			#Library of simple message tools

if __name__ == '__main__':

	rospy.init_node('robot_news_radio_transmitter', anonymous = True)   #Initializes the node (Also creates hides nodes from some subs)


	pub = rospy.Publisher("/robot_news_radio", String, queue_size = 10)  #rospy publisher class that contains topic data types queue size
	rate = rospy.Rate(2)		#Creates rate of .5 sec
	
	while not rospy.is_shutdown():	#While node is active
		msg = String()
		msg.data = "Greeting's, carbon-based lifeforms, this is Dan-Bot from Robot News Radio!"
		pub.publish(msg)	#Publishes message
		rate.sleep()

	rospy.loginfo("Node Communication Terminated #_#")
