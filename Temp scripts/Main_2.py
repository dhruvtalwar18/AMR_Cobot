#!/usr/bin/env python
import rospy
from math import sqrt

from std_msgs.msg import String
#Import srv
from std_msgs.msg import Int64
from nav_msgs.msg import Odometry
from actionlib_msgs.msg import GoalStatusArray
import actionlib
from actionlib_msgs.msg import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

class amr_movement:
    def __init__(self):
        rospy.init_node('main', anonymous=True)
        self.sub1 = rospy.Subscriber("product", String, self.sel)
        self.sub2 = rospy.Subscriber("odom", Odometry, self.nav_gen)
        self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        self.sub3 = rospy.Subscriber("move_base/status", GoalStatusArray, self.amr_stat)
        self.sub4 = rospy.Subscriber("PLC_output", GoalStatusArray, self.movebase_client_pick)
        self.pub = rospy.Publisher("goal_order", String, queue_size=10) # will send the ros service the order of points
        self.product_id = None
        self.product_list = set()
        self.temp = ''
        self.temp_dict = {}
        self.product_name = None
        self.GoalPointList = None  # The array containing the goal list to transverse
        self.current = None  # current coordinates of the bot
        self.nextGoal = None
        self.machineshop = None
        self.weldingshop = None
        self.grinding = None
        self.cobot_status = False
        self.amr_status = False
        self.shearing = None
        self.goaldict_flange = {'MS': [2.1, 2.2, 0.0], 'Welding shop': [6.5, 4.43, 0.0],
 'CNC_lathe': [4.5, 1.43, 0.0]}

    def sel(self, data):  # Robot to start which product to execute
        if data.data in ["flange","bike"]:
            if data.data == "flange":
                #print "Making a Hydraulic Flange"
                self.product_name = "flange"
            if data.data == "bike":
                #print "Making a Bike"
                self.product_name = "bike"
        else:
            pass
    def amr_stat(self,data):
        status = data
        if status.status_list[0].text == "Goal reached.":
            self.amr_status = True


    def nav_gen(self, odom_val):    # General Navigation for all
        self.current = [odom_val.pose.pose.position]
        if self.product_name == "flange":
            self.nav_flange()
        if self.product_name == "bike":
            self.nav_bike()

    def minimal(self, p1, p2):
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


    def movebase_client_station(self):
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = self.nextGoal[]
        if self.cobot_status == False:
            self.move_base.send_goal(goal)
            if self.cobot_status == False & self.amr_status == True:
                self.cobot_status = True
                cobot_action()

    def cobot_action(self):
        if self.product_name == "flange":
            #insert Omron procedure to follow
            self.cobot_status = False
            self.amr_status = False
            self.movebase_client_place()
        if self.product_name == 'bike':
            pass


    def movebase_client_place(self):

        for i in range(self.goaldict_flange):
            while self.cobot_status == False
            goal = MoveBaseGoal()
            goal.target_pose.header.frame_id = "map"
            goal.target_pose.header.stamp = rospy.Time.now()
            goal.target_pose.pose = self.nextGoal[]




    def movebase_client_pick(self, order_pick):
        target = order_pick
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = self.nextGoal[]
        if self.cobot_status == False:
            self.move_base.send_goal(goal)
            self.cobot_status = True
            self.cobot_action()



    def get_closest(self, req):
        pass


    def nav_flange(self):
        while self.cobot_status == False:
            self.movebase_client_station()
        while self.cobot_status = False :
            pass

        self.temp = String()
        self.temp.data = 'Working on a Hydraulic Flange'
        self.pub.publish(self.temp)



if __name__ == "__main__":
    rospy.init_node('main', anonymous=True)
    amr = amr_movement()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")




