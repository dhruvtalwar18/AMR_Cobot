#!/usr/bin/env python


import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import actionlib
import geometry_msgs

def simple_pick_place():
  moveit_commander.roscpp_initialize(sys.argv)
  rospy.init_node('simple_pick_place',
                  anonymous=True)


  robot1_group = moveit_commander.MoveGroupCommander("manipulator")




  robot1_client = actionlib.SimpleActionClient('execute_trajectory',
    moveit_msgs.msg.ExecuteTrajectoryAction)
  robot1_client.wait_for_server()
  rospy.loginfo('Execute Trajectory server is available for robot1')




  robot1_group.set_named_target("home")


  robot1_plan_home = robot1_group.plan()

  robot1_goal = moveit_msgs.msg.ExecuteTrajectoryGoal()

  robot1_goal.trajectory = robot1_plan_home


  robot1_client.send_goal(robot1_goal)
  robot1_client.wait_for_result()

  robot1_group.set_named_target("ready1")
  robot1_plan_pregrasp = robot1_group.plan()
  robot1_goal = moveit_msgs.msg.ExecuteTrajectoryGoal()
  robot1_goal.trajectory = robot1_plan_pregrasp
  robot1_client.send_goal(robot1_goal)
  robot1_client.wait_for_result()


  waypoints = []

  current_pose = robot1_group.get_current_pose()
  rospy.sleep(0.5)
  current_pose = robot1_group.get_current_pose()


  new_eef_pose = geometry_msgs.msg.Pose()


  new_eef_pose.position.x = current_pose.pose.position.x + 0.10
  new_eef_pose.position.y = current_pose.pose.position.y - 0.20
  new_eef_pose.position.z = current_pose.pose.position.z - 0.20


  new_eef_pose.orientation = copy.deepcopy(current_pose.pose.orientation)

  waypoints.append(new_eef_pose)
  waypoints.append(current_pose.pose)
  print(new_eef_pose.position)
  print(current_pose.pose.position)


  fraction = 0.0
  for count_cartesian_path in range(0,3):
    if fraction < 1.0:
      (plan_cartesian, fraction) = robot1_group.compute_cartesian_path(
                                    waypoints,
                                    0.01,
                                    0.0)
    else:
      break

  robot1_goal = moveit_msgs.msg.ExecuteTrajectoryGoal()
  robot1_goal.trajectory = plan_cartesian
  robot1_client.send_goal(robot1_goal)
  robot1_client.wait_for_result()

  robot1_group.set_named_target("ready2")
  robot1_plan_place = robot1_group.plan()
  robot1_goal = moveit_msgs.msg.ExecuteTrajectoryGoal()
  robot1_goal.trajectory = robot1_plan_place

  robot1_client.send_goal(robot1_goal)
  robot1_client.wait_for_result()
  moveit_commander.roscpp_shutdown()


if __name__=='__main__':
  try:
    simple_pick_place()
  except rospy.ROSInterruptException:
    pass
