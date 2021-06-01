#!/usr/bin/env python
import rospy
import sys
from std_msgs.msg import String
from nav_msgs.msg import Odometry


class amr_movement:
    def __init__(self):
        self.sub = rospy.Subscriber("product", String, self.sel)
        self.sub2 = rospy.Subscriber("odom", Odometry,self.nav_flange)
        self.product_id = None
        self.product_list = set()
        self.product_name = None
        self.GoalPointList = None # The array containing the goal list to transverse
        self.current = None # current coordinates of the bot
        self.nextGoal = None
        self.machineshop = None
        self.weldingshop = None
        self.grinding = None
        self.shearing = None
        self.goaldic = {'Machine shop': ["orientation"], 'Welding shop': ["orientation2"],'CNC_lathe': ["orientation3"]}



    def sel(self, data): # Robot to start which product to execute
        while True:
            if data.data not in set(self.product_list):
                self.product_list.add(data.data)
                if data.data == "flange":
                    print "Making a Hydraulic Flange"
                    
                if data.data == "bike":
                    self.bike()

            else:
                pass


    def nav_gen(self,data2):
        self.current = [data2.pose.pose.position]
        print self.current[0].x

    def bike(self):
        print " Making a Bike"


if __name__ == "__main__":
    amr = amr_movement()
    rospy.init_node('main', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")





