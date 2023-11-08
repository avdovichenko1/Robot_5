import rclpy, sys
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time


class CirclePublisher(Node):

    def __init__(self):
        super().__init__('publisher')
        self.publisher = self.create_publisher(Twist, '/robot/cmd_vel', 10)
        timer_period = 0.5  
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.flag = False
        
        
    def turns(self):
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = -0.5 
        self.publisher.publish(twist)
        self.flag=True
        time.sleep(5)
        
        
    def rasst(self):
        twist = Twist()
        twist.linear.x = 0.5
        twist.angular.z = 0.0        
        self.publisher.publish(twist)
        self.flag=False
        time.sleep(5)

    def timer_callback(self):
        twist = Twist()
        
        if self.flag==False:
            self.turns()
        else:
            self.rasst()
        
        
def main(args=None):
    rclpy.init(args=args)

    circling = CirclePublisher()

    rclpy.spin(circling)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
    
