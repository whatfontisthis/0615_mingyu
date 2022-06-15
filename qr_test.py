#!/usr/bin/env python3

import rospy
import cv2
from std_msgs.msg import String
from pyzbar.pyzbar import decode


def decoder(image):
    gray_img = cv2.cvtColor(image, 0)
    barcode = decode(gray_img)
    for obj in barcode:
        barcodeData = obj.data.decode("utf-8")
        print(barcodeData)

        rospy.init_node("pub_qr")
        pub = rospy.Publisher("qr_publisher", String, queue_size=1)
        qr_data = String()
        qr_data.data = barcodeData
        pub.publish(qr_data)


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    decoder(frame)
    cv2.imshow('Image', frame)  # show qr window
    code = cv2.waitKey(10)
    if code == ord('q'):
        break
