#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback_receive_radio_data(msg):	#Creation of the data callback function
	rospy.loginfo("Message Received: ")
	rospy.loginfo(msg)

if __name__ == '__main__':
	rospy.init_node('smartphone') 				#Note don't put "node" in node name

	sub = rospy.Subscriber("/robot_news_radio", String, callback_receive_radio_data) #Phone node is now sub of robot news node

	rospy.spin()  #Keeps scripts running until node is stopped
