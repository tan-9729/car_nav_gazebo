roslaunch test_car gazebo_my_car.launch                

rosrun teleop_twist_keyboard teleop_twist_keyboard.py

mapping:

roslaunch test_car create_house_and_car_map.launch

save_map:
rosservice call /finish_trajectory 0

rosservice call /write_state "{filename: '/home/tan/lerning_ws/src/test_car/maps/my_home2.pbstream'}"

rosrun cartographer_ros cartographer_pbstream_to_ros_map -map_filestem=${HOME}/lerning_ws/src/test_car/maps/my_home2 -pbstream_filename=${HOME}/lerning_ws/src/test_car/maps/my_home2.pbstream -resolution=0.05


nav:
roslaunch test_car nav.launch 
