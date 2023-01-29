import rclpy
import numpy as np
import tf_transformations as tf_trans

from rclpy.node        import Node
from geometry_msgs.msg import Vector3, Quaternion
from sensor_msgs.msg   import Joy
from tf2_ros           import TransformStamped, TransformBroadcaster


class control_your_robot(Node):
    def __init__(self,name):
        super().__init__(name)

        self.odom_broadcaster = TransformBroadcaster(self, 10)
        self.joystick_sub = self.create_subscription(Joy, 'joy', self.getJoystickInput, 10)

        self.scale_factor = 0.06

        # Attributes to define the starting position of the robot
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.theta = 0.0
        self.phi = 0.0
        self.psi = 0.0

        # Base transformation odom -> base
        self.odom_trans = TransformStamped()
        self.odom_trans.header.frame_id = "odom"
        self.odom_trans.child_frame_id = "base_link"

    def getJoystickInput(self, msg):
        self.x += self.scale_factor * msg.axes[1]
        self.y += self.scale_factor * msg.axes[0]

        self.broadcastTransformations()

    def broadcastTransformations(self):
        self.time_now = self.get_clock().now().to_msg()
        self.odom_trans.header.stamp = self.time_now
        self.odom_trans.transform.translation.x = self.x
        self.odom_trans.transform.translation.y = self.y
        self.odom_trans.transform.translation.z = 0.0

        q = tf_trans.quaternion_from_euler(0.0, 0.0, 0.0)

        self.odom_trans.transform.rotation = Quaternion(x = q[0],y = q[1],z = q[2],w = q[3])

        self.odom_broadcaster.sendTransform(self.odom_trans)

def main(args=None):
    rclpy.init(args=args)
    control_your1_robot = control_your_robot('your_first_robot')
    rclpy.spin(control_your1_robot) # equal to while true


if __name__=='__main__':
    main()