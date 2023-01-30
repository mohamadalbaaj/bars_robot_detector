# bars_robot_detector

## Setup
1. Create a workspace: `mkdir -p ~/ros2_ws/src` and access it with `cd ~/ros2_ws/src`
2. Create a package: `ros2 pkg create drobot --build-type ament_python`
3. Install the folders (meshes, launch, rviz, urdf) and files (bar.py, wall.py, joystick.py, distance_calculator.py) inside the package next to resource folder and __init__.py respectively.
4. Open the setup.py file and paste the code from the given file.

## Running the Package
1. Build the package: `colcon build --packages-select drobot`
2. Launch the package: `. install/setup.bash && ros2 launch drobot drobot_launch.py`
3. Run distance_calculator: `. install/setup.bash && ros2 run drobot distance_calculator`

## Object Names
- Workspace name: `ros2_ws`
- Package name: `drobot`
- Robot name: `bars_detector_robot`
- First object name: `wall`
- Second object name: `bar`

## To-Do List
- Write the documentation explaining the idea, procedure, tools and object parameters (required)
- Create a video to demonstrate the project and robot movement (required)
- Create slides for presentation (required)
- Edit the code of distance_calculator.py for accuracy (required)
- (Optional) Create a params.yaml file to edit parameters from one file.
- (Optional) Set range for detecting bars and export results in .csv file format.
- (Optional) Create setup.exe file with a good icon.
