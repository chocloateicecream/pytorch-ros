#! /usr/bin/env python 
import sys
import rospy
import cv2 
from sensor_msgs.msg import Image
import numpy as np 
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String 
import torch 

class torch_publisher: 
    def __init__(self):
        self.publisher=rospy.Publisher("img_message",Image,queue_size=10)
        self.bridge=CvBridge()

    def publish(self):
        img=cv2.imread("/home/lee/lena.jpg")
        img_torch=torch.from_numpy(img)
        img_torch[:,:,[0,2]]=img_torch[:,:,[2,0]]
        img_np=img_torch.numpy()
        # print(img_np)
        img_pub=self.bridge.cv2_to_imgmsg(img_np,"bgr8")
        self.publisher.publish(img_pub)

if __name__=="__main__":
    rospy.init_node('image_publisher',anonymous=True)
    publisher=torch_publisher()
    while not rospy.is_shutdown():
        publisher.publish()
        # print("done")
        rospy.Rate(10).sleep()
        