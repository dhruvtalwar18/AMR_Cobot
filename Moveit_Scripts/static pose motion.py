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

pose_target = geometry_msgs.msg.Pose()
pose_target.orientation.w = 0.30
pose_target.position.x = 0.5
pose_target.position.y = 0.1
pose_target.position.z = 0.5
manipulator.set_pose_target(pose_target)

plan = manipulator.plan()    #planning trajectory
manipulator.go(wait = True)
moveit_commander.roscpp_shutdown()
