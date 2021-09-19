#!/usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from geometry_msgs.msg import Pose
from moveit_commander.conversions import pose_to_list
from dh_gripper_msgs.msg import GripperCtrl
from tf.transformations import quaternion_from_euler
import time




class Omron:

  def __init__(self):
    #super(subscriber_class, self).__init__()

    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group_name = "manipulator"
    move_group = moveit_commander.MoveGroupCommander(group_name)
    display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)
    planning_frame = move_group.get_planning_frame()
    eef_link = move_group.get_end_effector_link()
    group_names = robot.get_group_names()
    print robot.get_current_state()

    self.move_group = move_group

  def go_to_pose_goal(self):
    grip = input("Choose this action; 0::Grip, 1::Release, 2::Movement only: ")
    pub = rospy.Publisher('/gripper/ctrl', GripperCtrl, queue_size=10)
    
    if grip == 0:
	omron.grip_complete()
    if grip == 1:
	omron.release_complete()
    if grip == 2:
	omron.move_complete()
    else:
	print "Please Type correctly"

  def grip_complete(self):
    

    
    if grip == 0:
	move_group = self.move_group
    	global pose_goal, count
    	pose_goal = Pose()

    	pose_goal.position.x = input('x coordinate: ')
    	pose_goal.position.y = input('y coordinate: ')
    	pose_goal.position.z = input('z coordinate: ')
    	roll = input("Enter Roll: ")
	pitch = input("Enter Pitch: ")
	yaw = input("Enter Yaw: ")
	quaternion = quaternion_from_euler(roll,pitch,yaw)
    	pose_goal.orientation.w = quaternion[3]
	pose_goal.orientation.x = quaternion[0]
	pose_goal.orientation.y = quaternion[1]
	pose_goal.orientation.z = quaternion[2]
    	rospy.loginfo(pose_goal)
    	move_group.set_pose_target(pose_goal)
	#r = rospy.Rate(10) #10hz
   	
    	plan = move_group.go(wait=True)
    	if (plan == True):
	    time.sleep(5)
	    msg = GripperCtrl()
    	    msg.initialize = False
    	    msg.speed = 100
    	    msg.force = 100
	    msg.position = 0 
            pub.publish(msg)
	    print "Item picked successfully"
    	else:
            print "Item could not be picked up"
    	move_group.stop()
    	move_group.clear_pose_targets()

    if grip == 1:
	move_group = self.move_group
    	global pose_goal, count
    	pose_goal = Pose()

    	pose_goal.position.x = input('x coordinate: ')
    	pose_goal.position.y = input('y coordinate: ')
    	pose_goal.position.z = input('z coordinate: ')
    	roll = input("Enter Roll: ")
	pitch = input("Enter Pitch: ")
	yaw = input("Enter Yaw: ")
	quaternion = quaternion_from_euler(roll,pitch,yaw)
    	pose_goal.orientation.w = quaternion[3]
	pose_goal.orientation.x = quaternion[0]
	pose_goal.orientation.y = quaternion[1]
	pose_goal.orientation.z = quaternion[2]
    	rospy.loginfo(pose_goal)
    	

    	move_group.set_pose_target(pose_goal)
	r = rospy.Rate(10) #10hz
   	 
    	plan = move_group.go(wait=True)
    	if (plan == True):
	    time.sleep(5)
	    msg = GripperCtrl()
    	    msg.initialize = False
    	    msg.speed = 100
    	    msg.force = 100
	    msg.position = 1000 
            pub.publish(msg)
            pub.publish(msg)
	    print "Item released successfully"
    	else:
            print "Item could not be released"
    	move_group.stop()
    	move_group.clear_pose_targets()


    if grip == 2:
	move_group = self.move_group
    	global pose_goal, count
    	pose_goal = Pose()

    	pose_goal.position.x = input('x coordinate: ')
    	pose_goal.position.y = input('y coordinate: ')
    	pose_goal.position.z = input('z coordinate: ')
	roll = input("Enter Roll: ")
	pitch = input("Enter Pitch: ")
	yaw = input("Enter Yaw: ")
	quaternion = quaternion_from_euler(roll,pitch,yaw)
    	pose_goal.orientation.w = quaternion[3]
	pose_goal.orientation.x = quaternion[0]
	pose_goal.orientation.y = quaternion[1]
	pose_goal.orientation.z = quaternion[2]
    	rospy.loginfo(pose_goal)
    	#pub_pose.publish(pose_goal)
    	#flag_plan = self._group.go(wait=True)

    	move_group.set_pose_target(pose_goal)
	r = rospy.Rate(10) #10hz
   	
    	plan = move_group.go(wait=True)
    	if (plan == True):
            print "moving to safe location"
    	else:
            print "Not able to move to safe location"
    	move_group.stop()
    	move_group.clear_pose_targets()


def main():
  try:
      while True:
          omron = Omron()
          print "============ Press `Enter` to execute a movement using a pose goal ============="          		
          raw_input()
          omron.go_to_pose_goal()
          ch = raw_input("Do you want to give more inputs (y/n): ")
          if ch == 'n':
              break

  except rospy.ROSInterruptException:
    return
  except KeyboardInterrupt:
    return

if __name__ == '__main__':
  main()
