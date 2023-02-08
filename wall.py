from visualization_msgs.msg import Marker
from rclpy.node             import Node
import numpy as np
import rclpy
import sys

class Wall(Node):

   def __init__(self, name):

      super().__init__(name)

      self.wall_pub = self.create_publisher(Marker, 'wall', 10)

      self.wall = Marker()
      self.wall.header.frame_id = "odom"
      self.wall.ns = "wall"
      self.wall.header.stamp = self.get_clock().now().to_msg()
      self.wall.id = 0
      self.wall.type = Marker().MESH_RESOURCE
      self.wall.action = Marker().ADD
      
      self.wall.pose.position.x = 3.6
      self.wall.pose.position.y = -0.07
      self.wall.pose.position.z = 0.7

      self.wall.pose.orientation.x = 0.0
      self.wall.pose.orientation.y = 0.0
      self.wall.pose.orientation.z = 0.0
      self.wall.pose.orientation.w = 1.0

      self.wall.scale.x = 1.0
      self.wall.scale.y = 1.0
      self.wall.scale.z = 1.0

      self.wall.color.a = 0.8
      self.wall.color.r = 0.52
      self.wall.color.g = 0.52
      self.wall.color.b = 0.52

      self.wall.mesh_resource = "package://drobot/meshes/wall.dae"


      timer_period = 2  # seconds
      self.timer = self.create_timer(timer_period, self.timer_callback)


   def timer_callback(self):

      self.wall_pub.publish(self.wall)

      #self.get_logger().info(f"I am alive")


def main(args=None):
   rclpy.init(args=args)
   obj1 = Wall('wall')

   try:
      rclpy.spin(obj1)

   except KeyboardInterrupt:

      print(f"Quitting wall prog")
      obj1.destroy_node()



   sys.exit(0)  

if __name__=='__main__':
   main()       

