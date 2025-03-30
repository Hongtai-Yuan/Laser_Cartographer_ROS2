# Laser_Cartographer_ROS2
基于cartgrapher和fishros，仓库在ros2humble中实现了手持雷达制图。简而言之，只需要雷达发布/scan主题，而不需要/odom就可以实现地图的构建。大部分参数都调整过了。它已经成功地在多个雷达上进行了测试。

<p align="center">
  <img src="readmefiles/1.png" width="500">
</p>

## 下载和使用
```bash
$ colcon build
$ . install/setup.bash
$ ros2 launch laser_cartographer cartographer_pure_laser.launch.py
```

## 如何保存地图？
```bash
$ ros2 run nav2_map_server map_saver_cli -f {mapname}.pgm
```

## 通常我们会使用GUN软件来对地图进行修正，这样就可以获得更好的导航效果
<p align="center">
  <img src="readmefiles/Snipaste_2024-12-14_23-13-47.jpg" width="200">
</p>


## 主要的参数(laser_2d.lua)
```bash
-- 0改成0.10,比机器人半径小的都忽略
TRAJECTORY_BUILDER_2D.min_range = 0.10
-- 30改成3.5,限制在雷达最大扫描范围内，越小一般越精确些
TRAJECTORY_BUILDER_2D.max_range = 20.0
-- 5改成3,传感器数据超出有效范围最大值
TRAJECTORY_BUILDER_2D.missing_data_ray_length = 5.
-- true改成false,不使用IMU数据
TRAJECTORY_BUILDER_2D.use_imu_data = false
-- false改成true,使用实时回环检测来进行前端的扫描匹配
TRAJECTORY_BUILDER_2D.use_online_correlative_scan_matching = true 
-- 1.0改成0.1,提高对运动的敏感度
-- TRAJECTORY_BUILDER_2D.motion_filter.max_angle_radians = math.rad(0.1)
-- 0.55改成0.65,Fast csm的最低分数，高于此分数才进行优化。
POSE_GRAPH.constraint_builder.min_score = 0.65
--0.6改成0.7,全局定位最小分数，低于此分数则认为目前全局定位不准确
POSE_GRAPH.constraint_builder.global_localization_min_score = 0.7
```
