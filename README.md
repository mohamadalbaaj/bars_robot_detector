# bars_robot_detector

## Prerequisites
- Ubuntu Linux operating system
- ROS2 Humble
### Required packages
Use the following command to install the necessary packages:
- sudo apt install ros-humble-urdf-tutorial
- sudo apt install joystick
- sudo apt install jstest-gtk
- sudo apt install ros-humble-joy-linux
- sudo apt install ros-humble-tf-transformations

Additionally, install the `transforms3d` package using the following command:
- sudo pip3 install transforms3d

### Hardware requirements
- Joystick

Note: Make sure to have the above mentioned software and hardware requirements before proceeding with the package.

## Setup
1. Create a workspace: `mkdir -p ~/ros2_ws/src` and access it with `cd ~/ros2_ws/src` (if you have ros2_ws already use another name)
2. Create a package: `ros2 pkg create drobot --build-type ament_python`
3. Install the folders (meshes, launch, rviz, urdf) inside the package (drobot), next to resource folder.
4. Install the files (bar.py, wall.py, enviroment.py, jointstate_joystick.py, distance_calculator.py) inside the package (drobot), again inside the folder (drobot), next to __init__.py.
5. Open the setup.py file in your package on your computer, copy and paste the code from the given file into your file.

## Running the Package
1. Access the workspace: `cd ~/ros2_ws`
2. Build the package: `colcon build --packages-select drobot`
3. Launch the package: `. install/setup.bash && ros2 launch drobot drobot_launch.py`
4. Run distance_calculator: `. install/setup.bash && ros2 run drobot distance_calculator`

## Object Names
1. Workspace name: `ros2_ws`
2. Package name: `drobot`
3. Robot name: `bars_detector_robot`
4. Base frame name:`odom`
5. First object name: `wall`
6. Second object name: `bar`
7. Third object name: `enviroment`
