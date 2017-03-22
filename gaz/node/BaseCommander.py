#!/usr/bin/env python
import rospy
from std_msgs.msg import String 
from sensor_msgs.msg import Range 
from geometry_msgs.msg import Twist 
from nav_msgs.msg import Odometry
from std_msgs.msg import Int8

	
		
global my_dire
my_dire = "none"


def sw_callback(swi):
    
    
    global sw
    sw = swi.data
    if sw == 'off':
    	move.linear.y = 0.0
    	
          
def odo_callback(bel):
	global my_dis
	my_dis = bel.pose.pose.position.y 
	
	
	    
def dir_callback(Direction):
	global my_dire
	global strih
	global b
	global fl
	my_dire = Direction.data
	if strih == 'none' :
		strih = my_dire
	if strih != my_dire :
		fl = True
		strih = my_dire
		rospy.logwarn(fl)
	else :
		fl = False
		
	

	'''
	rospy.logwarn(b)
	if strih != Direction.data :
		b = 1
	'''





	
	
	
def main():
	
	global velo_dis 
	velo_dis = 1
	global velocity_pub
	global sw
	move = Twist()
	global tempo
	global my_dire
	global fl
	fl = True
	global my_dis
	my_dis = 0
	#rospy.Subscriber('/distance', Int8, dis_callback)
	sw = 'off'
	rospy.Subscriber('/input', String , dir_callback)
	rospy.Subscriber('/switch', String , sw_callback)
	rospy.Subscriber('/odom', Odometry, odo_callback)
	rospy.init_node('BaseCommander', )
	rate = rospy.Rate(10)
	global b
	b = 1
	a = 1
	global strih
	strih = 'none'
	velocity_pub = rospy.Publisher('/cmd_vel',Twist, queue_size = 1)
	while True:

		#rospy.logwarn("loop")
		#rospy.logwarn(sw)
		#rospy.logwarn(my_dis)
		velocity_pub.publish(move)


		if ((my_dis >= 1 or my_dis <= -1 ) and a == 1) :
			b = 2

			if fl == True :
				fl = False
				b = 1
				a = 2

			
			move.linear.y = 0.0
			velocity_pub.publish(move)
			rospy.logwarn("maxmum position achieved cannot go further")
		
		
		else :
			if sw == 'on' and b == 1 :

				if my_dire == 'left'  :
					move.linear.y = 0.1
					if my_dis <= 0.8 and my_dis >= -0.8 :
						a = 1

					
				if my_dire == 'right' :
					move.linear.y = -0.1
					if my_dis <= 0.8 and my_dis >= -0.8 :
						a = 1

			#rospy.logwarn("Sitch on the node")

		pass
			

	while not rospy.is_shutdown():
		pass


if __name__ == '__main__':
    main()