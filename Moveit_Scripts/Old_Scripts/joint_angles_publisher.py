#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from moveit_msgs.msg import MotionPlanRequest

def talker():
    pub_angles = rospy.Publisher('publish_angles', JointState, queue_size=10)
    pub_velocity = rospy.Publisher('publish_velocities', MotionPlanRequest, queue_size=10)

    rospy.init_node('joint_angles_publisher', anonymous=True)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        joint_state_object = JointState()
        motion_plan_object = MotionPlanRequest()

        for i in range(6):
            #joint_state_object.name.append(raw_input('Name: '))
	    joint_state_object.position.append(input('Joint Angle (bottom up):'))
            #joint_state_object.velocity.append(input('Velocity: '))
            if i == 5:
                rospy.loginfo(joint_state_object.position)
                #rospy.loginfo(joint_state_object.velocity)

            pub_angles.publish(joint_state_object)

        motion_plan_object.max_velocity_scaling_factor = input('Velocity scaling factor (between 0 and 1): ')
        rospy.loginfo(motion_plan_object.max_velocity_scaling_factor)
        pub_velocity.publish(motion_plan_object)

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
