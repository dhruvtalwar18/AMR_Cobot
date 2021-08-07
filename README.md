# AMR and Cobot

The aim of the project is to integrate a working AMR and a ROS compatible cobot arm to develop a smart material handling robot capable of several mobile pick and place tasks.
The AMR will move in the factory floor and when an order is called the AMR shall go to a buffer station and intimate the ROS controlled cobot which shall then identify and pick the required raw material from the storage rack and place it on the AMR, then the AMR will take the product to the specific location where the raw material is needed.

The AMR is ROS based and the cobot is also developed around the ROS interface. 

<h1><b> ROS Cobot integration </h1></b>

The Omron Cobot that is used for this study is the TM5M-700 Cobot. The features for the same can be found out <a href="https://www.ia.omron.com/products/family/3739/feature.html">here </a>
 
Techman has provided ROS drivers and ROS packages for this cobot which can be found out <a href="https://github.com/TechmanRobotInc/tmr_ros1">here </a>

After the user has set up the ROS1 environment and built the TM driver based on the specific workspace, please enter your workspace <workspace> by launching the terminal, and remember to make the workspace visible to ROS. After cloning and building the repo, the cobot controller and the ubuntu system need to be connected via ethernet and the wired connection needs to be setup, instructions are given  <a href="https://github.com/TechmanRobotInc/tmr_ros1">here </a>

```
source /opt/ros/melodic/setup.bash
cd <workspace>
source ./devel/setup.bash
```  


Then, run the driver to maintain the connection with TM Robot by typing
```
  rosrun tm_driver tm_driver <robot_ip_address>
```
  
Once the setup is complete and we can ping the cobot IP, we shall use Move it, config launch files to move the Cobot. The Listen Node must be active in TMflow

```
  roslaunch tm5_700_moveit_config tm5_700_moveit_planning_execution.launch sim:=False robot_ip:=<robot_ip_address>
```
 
The simulation for the Cobot will open in Moveit and we can now move the actual robot by either moving the GUI cursor or using the Move Group Python Interface.  
  
We have developed scripts using the Move Group Python Interface, that will send user defined Joint angles or pose to the cobot and the cobot shall move accordingly.
The following will allow the user to control the cobot by publishing joint angles to the cobot. 
  
<p align = "center"> <img src="https://github.com/dhruvtalwar18/AMR_Cobot/blob/main/Moveit_integration_vids/ROS_Joint_Angle_Cobot_motion_Gif.gif" title="Result 1" width= "600" height = "350"></p>
<p align="center">Fig.1 OLP path of cobot simulation</p>


  




  

  
  
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
