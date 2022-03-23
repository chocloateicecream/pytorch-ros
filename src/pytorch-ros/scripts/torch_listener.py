#! /usr/bin/env python 
import sys
import rospy
import cv2 
from sensor_msgs.msg import Image
import numpy as np 
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String 
import torch 

class torch_subscriber:
    def __init__(self):
        self.subscriber=rospy.Subscriber("img_message",Image,self.callback)
        self.bridge=CvBridge()

    def callback(self,data):
        try: 
            cv_image=self.bridge.imgmsg_to_cv2(data,"bgr8")
        except CvBridgeError as e: 
            print(e)
        cv_image=torch.from_numpy(cv_image)
        torch_map=cv_image.transpose(0,2)
        print(torch_map.shape)

if __name__=="__main__":
    rospy.init_node("image_subscriber",anonymous=True)
    subscriber=torch_subscriber()
    rospy.spin()