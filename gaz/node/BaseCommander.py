#!/usr/bin/env python
import rospy
from std_msgs.msg import String 
from sensor_msgs.msg import Range 
from geometry_msgs.msg import Twist 

def dir_callback(direction):
    move = Twist()
    global velocity_pub
    if direction.data == 'left' :
        move.linear.y = 0.1
    if direction.data == 'right' :
        move.linear.y = -0.1
    velocity_pub.publish(move)
        
     
    
    
def main():
    global velocity_pub
    rospy.Subscriber('/input', String , dir_callback)
    rospy.init_node('BaseCommander', )
    rate = rospy.Rate(10)
    velocity_pub = rospy.Publisher('/cmd_vel',Twist, queue_size = 1)
    while not rospy.is_shutdown():
        pass


if __name__ == '__main__':
    main()