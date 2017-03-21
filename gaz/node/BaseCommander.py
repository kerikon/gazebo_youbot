#!/usr/bin/env python
import rospy

def main():
    rospy.init_node('BaseCommander')
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pass


if __name__ == '__main__':
    main()