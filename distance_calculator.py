import rclpy
from geometry_msgs.msg import Point, Vector3
from tf2_msgs.msg import TFMessage
from math import sqrt

def distance_between_point_and_line(p, lp, ld):
    return abs((p.x - lp.x) * ld.y - (p.y - lp.y) * ld.x) / sqrt(ld.x**2 + ld.y**2)

class DistanceCalculator:
    def __init__(self):
        self.node = rclpy.create_node('distance_calculator')
        self.subscriber = self.node.create_subscription(TFMessage, "tf", self.tf_callback, 10)
        self.line_point = Point(x=0.905, y=0.0, z=-0.31)
        self.line_direction = Vector3(x=0.000001, y=0.000001, z=-0.1)

    def tf_callback(self, msg):
        p1 = msg.transforms[0].transform.translation
        dist = distance_between_point_and_line(p1, self.line_point, self.line_direction)
        print("Distance between the point and the line: ", dist)

def main(args=None):
    rclpy.init(args=args)
    distance_calculator = DistanceCalculator()
    rclpy.spin(distance_calculator.node)
    distance_calculator.node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
