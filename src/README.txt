Önce gazebo çalıştır catkin_ws deyken yapabilirisn



export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch


sonra başka bir terminalde src dosyasının içine gir ve python kodunu çalıştır, gazebodan kontrol et


python3 pointtopoint.py 7 9 (7 ve 9 örnek onların yerine istediğin değer) 
