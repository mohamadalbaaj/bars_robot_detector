# bars_robot_detector

## Prerequisites
- Ubuntu Linux operating system
- ROS2 Humble
### Required packages
Use the following command to install the necessary packages:
sudo apt install ros-humble-urdf-tutorial
sudo apt install joystick
sudo apt install jstest-gtk
sudo apt install ros-humble-joy-linux
sudo apt install ros-humble-tf-transformations

Additionally, install the `transforms3d` package using the following command:
sudo pip3 install transforms3d

### Hardware requirements
- Joystick

Note: Make sure to have the above mentioned software and hardware requirements before proceeding with the package.

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

## To-Do List
1. Write the documentation explaining the idea, procedure, tools, and object parameters (required)
2. Create a video to demonstrate the project and robot movement (required)
3. Create slides for presentation (required)
4. (Optional) doing it for the rest of the bars in longitude and latitude.
5. (Optional) Create a params.yaml file to edit parameters from one file.
6. (Optional) Create setup.exe file with a good icon.
