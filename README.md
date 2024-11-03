ubuntu 20.04  
Gazebo 建模，cartography建图，多点导航  

gazebo环境：  
``` roslaunch test_car gazebo_my_car.launch```  

键盘控制节点：  
``` rosrun teleop_twist_keyboard teleop_twist_keyboard.py``` 

mapping 建图:    
``` roslaunch test_car create_house_and_car_map.launch``` 

save_map 保存地图（保存路径换成自己的）:  
``` rosservice call /finish_trajectory 0```   

``` rosservice call /write_state "{filename: '/home/user_name/lerning_ws/src/test_car/maps/my_home2.pbstream'}"```   

``` rosrun cartographer_ros cartographer_pbstream_to_ros_map -map_filestem=${HOME}/lerning_ws/src/test_car/maps/my_home2 -pbstream_filename=${HOME}/lerning_ws/src/test_car/maps/my_home2.pbstream -resolution=0.05```   

nav 导航:  
``` roslaunch test_car nav.launch ```   

获取当前机器人坐标文件：    
```rosrun test_car get_current_position.py```

坐标导航：    
```rosrun test_car navigate_to_goal.py```

多点坐标导航（我设置的三个点）：    
```rosrun test_car navigate_to_three_points.py```  

注意:    
python文件记得给权限  
cartographer包不含在本项目内，需要自己下载编译
