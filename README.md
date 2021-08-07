# AMR_Cobot

The aim is to integrate a working AMR and a cobot arm to develop a smart material handling robot capable of several mobile pick and place tasks.

We are using RoboDK for Offline Programming of the Omron TM5 Cobot. The following shows a demo of the cobot following a particular path

<p align = "center"> <img src="https://github.com/dhruvtalwar18/AMR_Cobot/blob/main/Images/Test_2_GOF.gif" title="Result 1" width= "600" height = "400"></p>
<p align="center">Fig.1 OLP path of cobot simulation</p>

This simulation demonstrates the integration of the DH robotics gripper with the Omron Cobot and shows the capabilities of the combined product
<p align = "center"> <img src="https://github.com/dhruvtalwar18/AMR_Cobot/blob/main/Images/Pick_place_cup.gif" title="Result 1" height = "400"></p>
<p align="center">Fig.2 Demo showing Gripping Action</p>


<h1><b> ROS Cobot integration </h1><b/>
  
 ```
$ echo hello
hello
```

The Omron Cobot that is used for this study is the TM5M-700 Cobot. It has ROS integration capabilties
We used the package https://github.com/TechmanRobotInc/tmr_ros1 for implementing the ROS connection with the robot.
  
  
This simulation demonstrates the integration of the DH robotics gripper with the Omron Cobot and shows the capabilities of the combined product
<p align = "center"> <img src="https://github.com/dhruvtalwar18/AMR_Cobot/blob/main/Demo%20Vids/ROS_COBOT_TEST_1.gif" title="Result 2 height = "400"></p>
<p align="center">Fig.3 Moveit Integration with actual Cobot </p>
