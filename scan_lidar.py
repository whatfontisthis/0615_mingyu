#! /usr/bin/python3

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32
import numpy as np

distance = 0


def talker(dis):
    pub = rospy.Publisher('scan_publisher', Float32, queue_size=1)
    msg = Float32()
    msg.data = dis
    pub.publish(msg)
    print("msg published")


def laser_callback(data):
    global distance

    #distance in cm
    distance = round(np.mean(np.setdiff1d(
        data.ranges[:25] + data.ranges[-25:], [0]))*100, 2)
    #distance = data.ranges[0]
    print(distance)
    talker(distance)


if __name__ == '__main__':
    rospy.init_node('scan_forward', anonymous=True)
    rospy.Subscriber('/scan', LaserScan, laser_callback)
    rospy.spin()
