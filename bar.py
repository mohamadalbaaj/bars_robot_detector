from visualization_msgs.msg  import Marker, MarkerArray
import rclpy
from rclpy.node import Node
import numpy as np

class Bar(Node):
    def __init__(self,name):
        super().__init__(name)

        self.bar_pub = self.create_publisher(MarkerArray, 'bar', 10)

        self.timer = self.create_timer(2.0, self.timer_callback)

        self.array = MarkerArray()

        for i in range(5):

            self.bar = Marker()
            self.bar.header.frame_id = 'odom'
            self.bar.ns = 'bar'
            self.bar.header.stamp = self.get_clock().now().to_msg()
            self.bar.id = i            
            self.bar.type = Marker().MESH_RESOURCE
            self.bar.action = Marker().ADD

            self.bar.pose.position.x = 2.0
            self.bar.pose.position.y = i * 0.3
            self.bar.pose.position.z = 1.0

            self.bar.pose.orientation.x = 0.0
            self.bar.pose.orientation.y = 0.0
            self.bar.pose.orientation.z = 0.0
            self.bar.pose.orientation.w = 1.0

            self.bar.scale.x = 1.0
            self.bar.scale.y = 1.0
            self.bar.scale.z = 1.0

            self.bar.color.a = 1.0
            self.bar.color.r = 0.5
            self.bar.color.g = 0.5
            self.bar.color.b = 0.0

            self.bar.mesh_resource = "package://drobot/meshes/bar.dae"

            self.array.markers.append(self.bar)
            
            self.bar = Marker()
            self.bar.header.frame_id = 'odom'
            self.bar.ns = 'bar'
            self.bar.header.stamp = self.get_clock().now().to_msg()
            self.bar.id = -i            
            self.bar.type = Marker().MESH_RESOURCE
            self.bar.action = Marker().ADD

            self.bar.pose.position.x = 2.0
            self.bar.pose.position.y = -i * 0.3
            self.bar.pose.position.z = 1.0

            self.bar.pose.orientation.x = 0.0
            self.bar.pose.orientation.y = 0.0
            self.bar.pose.orientation.z = 0.0
            self.bar.pose.orientation.w = 1.0

            self.bar.scale.x = 1.0
            self.bar.scale.y = 1.0
            self.bar.scale.z = 1.0

            self.bar.color.a = 1.0
            self.bar.color.r = 0.5
            self.bar.color.g = 0.5
            self.bar.color.b = 0.0

            self.bar.mesh_resource = "package://drobot/meshes/bar.dae"

            self.array.markers.append(self.bar)

    def timer_callback(self):
        self.bar_pub.publish(self.array)

     

def main(args=None):
    rclpy.init(args=args)
    bar = Bar('bar')
    try:
        rclpy.spin(bar)
    except KeyboardInterrupt:
        print(f"quitting the program...")
        bar.destroy_node()
    exit(0)


if __name__=='__main__':
   main() 
