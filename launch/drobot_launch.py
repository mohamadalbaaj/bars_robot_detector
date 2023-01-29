from ament_index_python.packages       import get_package_share_path

from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions                import Node
from launch.substitutions              import Command, LaunchConfiguration
from launch.actions                    import DeclareLaunchArgument, ExecuteProcess
from launch                            import LaunchDescription

import os


# The following function is mandatory
def generate_launch_description():

    # Defining the object, which must be returned
    ld = LaunchDescription()

    package_path = get_package_share_path('drobot')

    urdf_model_path  = os.path.join(package_path, 'urdf/bars_detector_robot.urdf')

    rviz_config_path = os.path.join(package_path, 'rviz/config.rviz')

    model_arg = DeclareLaunchArgument(name          = 'bars_detector_robot',
                                      default_value = str(urdf_model_path),
                                      description   = "This is my URDF model definition")

    rviz_arg = DeclareLaunchArgument(name          = 'rvizconfig',
                                     default_value = str(rviz_config_path),
                                     description   = "This is my RViz config file")

    robot_description = ParameterValue(Command(['xacro ', LaunchConfiguration('bars_detector_robot')]),
                                       value_type = str)

    # joystick
    joystick_node = Node(package    = "drobot",
                         executable = "joystick",
                         output     = "screen",
                         namespace  = None)


    # Configure the robot_state_publisher
    robot_state_node = Node(package    = "robot_state_publisher",
                            executable = "robot_state_publisher",
                            name       = "robot_state_publisher",
                            output     = "screen",
                            parameters = [{'robot_description': robot_description}])

    # Configure the node for the joystick
    joy_node = Node(package    = "joy",
                    executable = "joy_node",
                    output     = "screen",
                    namespace  = None)

    # Configure RViz for visualization
    rviz_node = Node(package    = "rviz2",
                     executable = "rviz2",
                     output     = "screen",
                     namespace  = None,
                     arguments  = ["-d", LaunchConfiguration("rvizconfig")])

    # Configure the joint_state_publisher_gui
    joint_state = Node(package     = "joint_state_publisher_gui",
                        executable = "joint_state_publisher_gui",
                        name       = "joint_state_publisher_gui",
                        output     = "screen")

    # static_transform_publisher
    node = Node(package    = "tf2_ros",
                executable = "static_transform_publisher",
                output     = "screen",
                arguments  = ["0", "0", "0", "0", "0", "0","odom","head"]
                )

    # wall
    wall_node = Node(package    = "drobot",
                     executable = "wall",
                     output     = "screen",
                     namespace  = None)

    # bar
    bar_node = Node(package     = "drobot",
                     executable = "bar",
                     output     = "screen",
                     namespace  = None)

    # distance_calculator
    distance_calculator_node = Node(package     = "drobot",
                                     executable = "distance_calculator",
                                     output     = "screen",
                                     namespace  = None)


    ld.add_action(model_arg)
    ld.add_action(rviz_arg)
    ld.add_action(joystick_node)
    ld.add_action(robot_state_node)
    ld.add_action(joint_state)
    ld.add_action(joy_node)
    ld.add_action(rviz_node)
    ld.add_action(node)
    ld.add_action(wall_node)
    ld.add_action(bar_node)
    #ld.add_action(distance_calculator_node)


    return ld