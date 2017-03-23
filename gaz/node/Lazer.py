#!/usr/bin/env python
import rospy
from std_msgs.msg import String 
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist 
from nav_msgs.msg import Odometry
from std_msgs.msg import Int8

	
		
global my_dire
my_dire = "none"

def la_callback(ls_d):
	ran = ls_d.ranges
	min_d = min(ran)
	i = 0
	global mn
	mn = False
	if min_d <= 0.10
		for i in range[55 , 145]:
			if ran[i] < 0.10 :
				mn = True


	rospy.logwarn(ls_d.angle_min)



	
         
def odo_callback(bel):
	global my_dis
	my_dis = bel.pose.pose.position.y 
	
	

	
def main():
	global mn
		
	rospy.Subscriber('base_scan', LaserScan, la_callback)
	rospy.Subscriber('/odom', Odometry, odo_callback)
	rospy.init_node('Lazer' , )
	rate = rospy.Rate(10)
	while True:
		if mn == True :
			


		velocity_pub = rospy.Publisher('/cmd_vel',Twist, queue_size = 1)
	pass
	
	while not rospy.is_shutdown():
		pass


if __name__ == '__main__':
    main()