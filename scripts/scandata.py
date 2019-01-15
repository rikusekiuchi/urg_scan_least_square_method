#!/usr/bin/env python
import rospy
import math
import numpy as np
import matplotlib.pyplot as plt
from sensor_msgs.msg import LaserScan

def recv_sendata(data):

    distance_data = np.array([])

    for i in range(1,2):
        aa = data.ranges[384]

        distance_data = np.append(distance_data, aa)
 
    print(distance_data)
    print('hello')

if __name__ == '__main__:':
    rospy.init_node('scan_sub')
    rospy.Subscriber("scan", LaserScan, recv_sendata)
    r = rospy.Rate(10)
    r.sleep()
    rospy.spin()
