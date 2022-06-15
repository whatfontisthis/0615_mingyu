#!/usr/bin/env python

import rospy
import cv2
from std_msgs import Float32, String


def cb_scan(msg):
    pass


def cb_qr(msg):
    pass


def talker():
    pub = rospy.init_node("check_point", anonymous=True)
    rospy.Publisher("check_point", String, queue_size=1)
    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        pub.publish()


def listener():
    rospy.Subscriber('/scan_publisher', Float32, cb_scan)
    rospy.Subscriber('/qr_publisher', String, cb_qr)


if __name__ == "__main__":
    talker()
