# bars_robot_detector

## Setup
1. Create a workspace: `mkdir -p ~/ros2_ws/src` and access it with `cd ~/ros2_ws/src`
2. Create a package: `ros2 pkg create drobot --build-type ament_python`
3. Install the folders (meshes, launch, rviz, urdf) inside the package (drobot), next to resource folder.
4. Install the files (bar.py, wall.py, joystick.py, distance_calculator.py) inside the package (drobot), again inside the folder (drobot), next to __init__.py.
5. Open the setup.py file in your package on your computer, copy and paste the code from the given file into your file.

## Running the Package
1. Access the workspace: `cd ~/ros2_ws`
2. Build the package: `colcon build --packages-select drobot`
3. Launch the package: `. install/setup.bash && ros2 launch drobot drobot_launch.py`
4. Run distance_calculator: `. install/setup.bash && ros2 run drobot distance_calculator.py`

## Object Names
1. Workspace name: `ros2_ws`
2. Package name: `drobot`
3. Robot name: `bars_detector_robot`
4. First object name: `wall`
5. Second object name: `bar`

## To-Do List
1. Write the documentation explaining the idea, procedure, tools, and object parameters (required)
2. Create a video to demonstrate the project and robot movement (required)
3. Create slides for presentation (required)
4. Edit the code of distance_calculator.py for accuracy (required)
5. (Optional) Create a params.yaml file to edit parameters from one file.
6. (Optional) Set range for detecting bars and export results in .csv file format.
7. (Optional) Create setup.exe file with a good icon.
