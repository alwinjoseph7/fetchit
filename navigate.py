import numpy as np
import cv2
from collections import deque

def nav(imageFrame):
    linecolor = (100, 215, 255)
    pts = deque(maxlen=7)

    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    lower = np.array([4, 106, 105], np.uint8)
    upper = np.array([28, 255, 255], np.uint8)
    mask = cv2.inRange(hsvFrame, lower, upper)

    kernal = np.ones((5, 5), "uint8")
    
    mask = cv2.dilate(mask, kernal)
    res1 = cv2.bitwise_and(imageFrame, imageFrame,mask = mask)
    
    res = cv2.GaussianBlur(res1,(5,5),0)

    edged = cv2.Canny(res, 20, 50)
    cv2.imshow("edges", edged)
    cv2.imshow("mask", res)
    cnts, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    cnts.sort (key = lambda x: cv2.contourArea (x), reverse = True)
    out = np.zeros_like (mask)
    cv2.drawContours(imageFrame, [cnts [0]], -1, color = 255, thickness = 2)
    cv2.drawContours(imageFrame, [cnts [1]], -1, color = 255, thickness = 2)

    if len(cnts) > 0:

        ((x, y), radius) = cv2.minEnclosingCircle(cnts[0])
        M = cv2.moments(cnts[0])
        center1 = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        
    pts.append(center1)
    if len(cnts) > 0:

        ((x, y), radius) = cv2.minEnclosingCircle(cnts[1])
        M = cv2.moments(cnts[1])
        center2 = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
       
    pts.append(center2)
    cv2.line(imageFrame, (center1), (center2), (0, 255, 0), thickness=3, lineType=8)

    slope = (center1[1]-center2[1])/(center1[0]-center2[0])

    if slope > 0.1:
        print("\tRight")

    elif slope < -0.1:
        print("\tLeft")
    
    else: 
        print("\tStraight")
    cv2.imshow("video", imageFrame)
