import rclpy
import numpy as np
import tf_transformations as tf_trans

from rclpy.node        import Node
from geometry_msgs.msg import Vector3, Quaternion
from sensor_msgs.msg   import Joy, JointState
from tf2_ros           import TransformStamped, TransformBroadcaster


class control_your_robot(Node):
    def __init__(self,name):
        super().__init__(name)

        self.odom_broadcaster = TransformBroadcaster(self, 10)
        self.joint_state_pub = self.create_publisher(JointState, 'joint_states', 10)
        self.joystick_sub = self.create_subscription(Joy, 'joy', self.getJoystickInput, 10)

        self.scale_factor = 0.02

        # Attributes to define the starting position of the robot
        self.x = 0.0
        self.y = 0.0
        self.sa = 0.0
        self.a2h = 0.0
        self.front_left_wheel_joint = 0.0
        self.front_right_wheel_joint = 0.0
        self.rear_left_wheel_joint = 0.0
        self.front_left_wheel_joint = 0.0
        self.bs = 0.0
        self.a1m = 0.0
        self.ma2 = 0.0
        self.main = 0.0
        self.mainn = 0.0

        # Base transformation odom -> base
        self.odom_trans = TransformStamped()
        self.odom_trans.header.frame_id = "odom"
        self.odom_trans.child_frame_id = "base_link"

        # Definition attributes for the joints state transformations

        self.jointstate = JointState()
        self.jointstate.name = ["front_left_wheel_joint", "front_right_wheel_joint", "rear_left_wheel_joint", "rear_right_wheel_joint" ,"bs", "sa", "a1m","ma2", "a2h", "main", "mainn"]

    def getJoystickInput(self, msg):
        self.x += self.scale_factor * msg.axes[1]
        self.y += self.scale_factor * msg.axes[0]
        self.sa += msg.axes[2]
        self.a2h += msg.axes[3]

        self.broadcastTransformations()

    def broadcastTransformations(self):
        self.time_now = self.get_clock().now().to_msg()
        self.odom_trans.header.stamp = self.time_now
        self.odom_trans.transform.translation.x = self.x
        self.odom_trans.transform.translation.y = self.y


        self.odom_broadcaster.sendTransform(self.odom_trans)

        self.jointstate.header.stamp = self.time_now
        self.jointstate.position = [0.0, 0.0, 0.0, 0.0, 0.0, np.radians(self.sa), 0.0, 0.0, np.radians(self.a2h), 0.0, 0.0]

        self.joint_state_pub.publish(self.jointstate)

def main(args=None):
    rclpy.init(args=args)
    control_your1_robot = control_your_robot('joint_state_joystick')
    rclpy.spin(control_your1_robot) # equal to while true


if __name__=='__main__':
    main()
