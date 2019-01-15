#!/usr/bin/env python
import rospy
import math
import numpy as np
import matplotlib.pyplot as plt
from sensor_msgs.msg import LaserScan

def recv_sendata(data):

    X = np.array([])
    Y = np.array([])

    for i in range(256, 512):
        scan_array = data.ranges[i]
        if math.isnan(scan_array):
            scan_array = 0

        if scan_array > 0:
            scan_angle = i-128

            scan_cos = math.cos(math.radians(scan_angle*0.35190616))
            scan_sin = math.sin(math.radians(scan_angle*0.35190616))

            x = scan_array*scan_cos
            y = scan_array*scan_sin

            X = np.append(X, x)
            Y = np.append(Y, y)

    A = np.array([X,np.ones(len(X))])
    A = A.T
    a,b = np.linalg.lstsq(A,Y)[0]
    print'y=',a,'x +',b
    
    rad = math.atan(a)
    deg = math.degrees(rad)

    print'rad=',rad
    print'deg=',deg

    result = 90-deg
    print'result=',result    

    plt.plot(X,Y, 'ro')
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.plot(X,(a*X+b),"g--")
    plt.show()



if __name__ == '__main__':
    try:
        rospy.init_node('scan_sub')
        rospy.Subscriber("scan", LaserScan, recv_sendata)
        r = rospy.Rate(10)
        r.sleep()
        rospy.spin()

    except rospy.ROSInterruptException: pass
