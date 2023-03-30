# PtoP
This is a robot programming project using
 
-Gazebo 
-Ros noetic
-Ubuntu 20.04
-Turtlebot3

->First the project will be installed inside a folder named catkin_ws. I call the folder catkin_ws from now.
->On terminal, change directory to catkin_ws.

$cd catkin_ws

->Then run the following commands to determine the arguments and start a burger turtlebot in a empty bot.

$export TURTLEBOT3_MODEL=burger
$roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch

->Now on a different terminal chaenge directory to catkin_ws/src to run the python code.

$cd catkin_ws/src 

->Run the python code with the arguments x and y axis points respectively. (x=7 y=9 example) 
$python3 pointtopoint.py 7 9 

 
