# bars_robot_detector

steps to setup the package:

1) create a workspace:

mkdir -p ~/ros2_ws/src

and access the work space

cd ~/ros2_ws/src

2) create a package:

ros2 pkg create drobot --build-type ament_python

3) install the folders (meshes, launch, rviz, urdf) inside the package (drobot), next to resource folder

4) install the files (bar.py, wall.py, joystick.py, distance_calculator.py) inside the package (drobot), again inside the folder (drobot), next to __init__.py

5) open the setup.py file in your package on your computer, copy and paste the code from the file here into your file


steps to run the package: open the terminal and access the workspace (cd ~/ros2_ws)

1)in the first terminal type (colcon build --packages-select drobot)

2)in the second terminal type (. install/setup.bash && ros2 launch drobot drobot_launch.py)

3)in the third terminal type (. install/setup.bash && ros2 run drobot distance_calculator)


object names:

name of the workspace: ros2_ws
name of the package: drobot
name of the robot: bars_detector_robot
name of the first object: wall
name of the second object: bar


