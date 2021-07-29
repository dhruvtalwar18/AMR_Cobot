#!/usr/bin/env python
#!/usr/bin/env python2
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from sensor_msgs.msg import JointState
from moveit_msgs.msg import MotionPlanRequest
from moveit_commander.conversions import pose_to_list

def callback_angles(joint_object):
    global count, joint_goal
    count += 1
    joint_goal = joint_object.position
    rospy.loginfo(rospy.get_caller_id() + " Angle: %f", joint_object.position[-1])

def listener_angles():
    global count
    sub_angles = rospy.Subscriber('publish_angles', JointState, callback_angles)
    while not count == 6:
        rospy.rostime.wallsleep(0.5)
    sub_angles.unregister()

def callback_vel(motion_plan_obj):
    global scaling_factor, count
    count += 1
    scaling_factor = motion_plan_obj.max_velocity_scaling_factor
    rospy.loginfo(rospy.get_caller_id() + " Scaling factor: %f", scaling_factor)

def listener_vel():
    global count
    sub_vel = rospy.Subscriber('publish_velocities', MotionPlanRequest, callback_vel)
    while not count == 1:
        rospy.rostime.wallsleep(0.5)
    sub_vel.unregister()

class subscriber(object):

  def __init__(self):
    super(subscriber, self).__init__()

    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('joint_angles_subscriber', anonymous=True)

    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group_name = "manipulator"
    move_group = moveit_commander.MoveGroupCommander(group_name)
    display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)

    planning_frame = move_group.get_planning_frame()
    # print "============ Reference frame: %s" % planning_frame
    eef_link = move_group.get_end_effector_link()
    #print "============ End effector: %s" % eef_link
    group_names = robot.get_group_names()
    # print "============ Robot Groups:", robot.get_group_names()
    print "============ Printing robot state"
    print robot.get_current_state()
    # print ""

    self.move_group = move_group

  def go_to_joint_state(self):
    move_group = self.move_group
    global joint_goal, count, scaling_factor

    scaling_factor = 1
    joint_goal = move_group.get_current_joint_values()

    count = 0
    listener_angles()

    count = 0
    listener_vel()

    move_group.set_max_velocity_scaling_factor(scaling_factor)
    move_group.go(joint_goal, wait=True)
    move_group.stop()

def main():
  try:
    while True:
        subscriber_object = subscriber()
        print "============ Press `Enter` to execute a movement using a joint state goal: "
        raw_input()
        subscriber_object.go_to_joint_state()
        ch = raw_input("Do you want to give more inputs (y/n): ")
        if ch == 'n':
            break

  except rospy.ROSInterruptException:
    return
  except KeyboardInterrupt:
    return

if __name__ == '__main__':
  main()
