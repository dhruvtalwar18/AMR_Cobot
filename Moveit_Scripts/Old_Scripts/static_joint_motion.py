#!/usr/bin/env python2
import sys
import copy
import rospy
import random
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_interface', anonymous = True)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
print "Group names are: %s" % "," .join(robot.get_group_names())   # Check for groupnames
manipulator = moveit_commander.MoveGroupCommander("manipulator")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory, queue_size = 1)


group_variable_values = manipulator.get_current_joint_values()

group_variable_values[0] = 1.5
group_variable_values[1] = 0
group_variable_values[3] = -1.5
group_variable_values[5] = 1.5
manipulator.set_joint_value_target(group_variable_values)

plan2 = manipulator.plan()
manipulator.go(wait=True)

rospy.sleep(5)

moveit_commander.roscpp_shutdown()


