import numpy as np
import cv2
import argparse
from collections import deque

video = cv2.VideoCapture("path.mp4")
linecolor = (100, 215, 255)
pts = deque(maxlen=7)
while(1):
    
    ret, imageFrame = video.read()
    if not ret:
        video=cv2.VideoCapture("path.mp4")
        continue


    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    lower = np.array([10, 100, 20], np.uint8)
    upper = np.array([25, 255, 255], np.uint8)
    mask = cv2.inRange(hsvFrame, lower, upper)

    kernal = np.ones((5, 5), "uint8")
    

    mask = cv2.dilate(mask, kernal)
    res = cv2.bitwise_and(imageFrame, imageFrame,
                            mask = mask)
    edged = cv2.Canny(res, 1, 1)
    cv2.imshow("edges", edged)
    cv2.imshow("mask", mask)

    cnts, hierarchy = cv2.findContours(mask,
                                        cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_SIMPLE)
    
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius > 5:
            cv2.circle(imageFrame, (int(x), int(y)), int(radius), (255, 255, 255), 2)
            cv2.circle(imageFrame, center, 5, linecolor, -1)
    pts.append(center)
    for i in range(1, len(pts)):
        if pts[i - 1] is None or pts[i] is None:
            continue
        thick = 3
        cv2.line(imageFrame, pts[i - 1], pts[i], linecolor, thick)

            
    # Program Termination
    cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        video.release()
        cv2.destroyAllWindows()
        break
