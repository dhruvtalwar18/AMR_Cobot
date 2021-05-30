#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int8



def callback(msg):   #function callback which recieves a parameters named msg
  prod = msg.data
  amr_dict = {}
  amr_dict = {'flange': "location1", 'bike': 'location 2'}
  
  #Call ROS service to send the AMR to the pose position	
     
 

  while amr_get_status is not False:
  
  

if __name__=='__main__':
  rospy.init_node('product')
  product = rospy.Subscriber('product', Int8, callback)
  amr_loc = rospy.Publisher('amr', String, queue_size= 1)
  cobot_work = rospy.Publisher('cobot', String, queue_size=1)
  rospy.spin()
  
  
