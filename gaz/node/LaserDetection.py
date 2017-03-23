#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist 
from nav_msgs.msg import Odometry

class LaserDetection:
    def laser_front_callback(self, scan):
        move = Twist()
        ranges = scan.ranges[60:120]
        dist = 0.3
        self.detectedFront = False
        
        for i in ranges:
            if (i < scan.range_max) & (i > scan.range_min) & (i < dist):
                self.detectedFront = True

        if self.detectedFront & (not self.detectedBack) & (not self.movingBack) & (not self.movingForward):
            move.linear.x = -0.1
            rospy.logwarn("Moving back!")
            self.positionToGo = self.distance - dist
            self.movingBack = True
            self.movement_publisher.publish(move)
        elif self.detectedFront & self.movingForward:
            move.linear.x = 0
            self.movingForward = False
            self.movement_publisher.publish(move)
        elif self.movingBack:
            if(self.distance < self.positionToGo):
                move.linear.x = 0
                self.movingBack = False
                self.movement_publisher.publish(move)

    def laser_back_callback(self, scan):
        move = Twist()
        ranges = scan.ranges[60:120]
        dist = 0.3
        self.detectedBack = False
        
        for i in ranges:
            if (i < scan.range_max) & (i > scan.range_min) & (i < dist):
                self.detectedBack = True

        if self.detectedBack & (not self.detectedFront) & (not self.movingBack) & (not self.movingForward):
            move.linear.x = 0.1
            rospy.logwarn("Moving forward!")
            self.positionToGo = self.distance + dist
            self.movingForward = True
            self.movement_publisher.publish(move)
        elif self.detectedBack & self.movingBack:
            move.linear.x = 0
            self.movingBack = False
            self.movement_publisher.publish(move)
        elif self.movingForward:
            if(self.distance > self.positionToGo):
                move.linear.x = 0
                self.movingForward = False
                self.movement_publisher.publish(move)

    def odometry_callback(self, odometry):
        self.distance = odometry.pose.pose.position.x
    
    def __init__(self):
        self.lazer_front_subscriber = rospy.Subscriber("/base_scan", LaserScan, self.laser_front_callback)
        self.lazer_back_subscriber = rospy.Subscriber("/base_scan_back", LaserScan, self.laser_back_callback)
        self.odometry_subscriber = rospy.Subscriber("/odom", Odometry, self.odometry_callback)
        self.movement_publisher = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)
        self.distance = 0
        self.movingBack = False
        self.movingForward = False
        self.detectedFront = False
        self.detectedBack = False
        self.positionToGo = 0
	
		
def main():
    rospy.init_node("LaserDetection")
    
    laser = LaserDetection()
	
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rate.sleep()
    pass


if __name__ == '__main__':
    main()
