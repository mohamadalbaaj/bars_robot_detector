from visualization_msgs.msg import Marker
from rclpy.node             import Node
import numpy as np
import rclpy
import sys

class Enviroment(Node):

   def __init__(self, name):

      super().__init__(name)

      self.enviroment_pub = self.create_publisher(Marker, 'enviroment', 10)

      self.enviroment = Marker()
      self.enviroment.header.frame_id = "odom"
      self.enviroment.ns = "enviroment"
      self.enviroment.header.stamp = self.get_clock().now().to_msg()
      self.enviroment.id = 0
      self.enviroment.type = Marker().MESH_RESOURCE
      self.enviroment.action = Marker().ADD
      
      self.enviroment.pose.position.x = 0.0
      self.enviroment.pose.position.y = 0.0
      self.enviroment.pose.position.z = -0.1

      self.enviroment.pose.orientation.x = 0.0
      self.enviroment.pose.orientation.y = 0.0
      self.enviroment.pose.orientation.z = 0.0
      self.enviroment.pose.orientation.w = 1.0

      self.enviroment.scale.x = 1.0
      self.enviroment.scale.y = 1.0
      self.enviroment.scale.z = 1.0

      self.enviroment.color.a = 1.0
      self.enviroment.color.r = 0.5
      self.enviroment.color.g = 0.5
      self.enviroment.color.b = 0.5

      self.enviroment.mesh_resource = "package://drobot/meshes/enviroment.dae"


      timer_period = 2  # seconds
      self.timer = self.create_timer(timer_period, self.timer_callback)


   def timer_callback(self):

      self.enviroment_pub.publish(self.enviroment)

      #self.get_logger().info(f"I am alive")


def main(args=None):
   rclpy.init(args=args)
   obj1 = Enviroment('enviroment')

   try:
      rclpy.spin(obj1)

   except KeyboardInterrupt:

      print(f"Quitting enviroment prog")
      obj1.destroy_node()



   sys.exit(0)  

if __name__=='__main__':
   main()       

