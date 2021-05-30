#!/usr/bin/env python

import rospy

from std_msgs.msg import String
from std_msgs.msg import Int8

prod = ''

def select():
  global prod
  my_dict = {1: 'flange', 2: 'bike'}
  value = input("Which product you wish to select ")
  print "Product selected",my_dict[value]
  prod = my_dict[value] 


	    
 
def action_create():
  rospy.init_node('product')
  pub = rospy.Publisher('product',String, queue_size= 1)
  while not rospy.is_shutdown():
        prdt = prod
        pub.publish(prdt)




if __name__=='__main__':
  select()
  action_create()
  rospy.spin()
  
  
