import cv2
import serial
import numpy as np

video = cv2.VideoCapture(0)
Ser = serial.Serial("/dev/ttyACM0", baudrate=9600)
Ser.flush()

while True:    
    flag, imageFrame = video.read()
    if not flag:
        _, imageFrame = video.read()

    linecolor = (100, 215, 255)
    
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    lower = np.array([4, 106, 105], np.uint8)
    upper = np.array([28, 255, 255], np.uint8)
    mask = cv2.inRange(hsvFrame, lower, upper)

    kernal = np.ones((5, 5), "uint8")
    
    mask = cv2.dilate(mask, kernal)
    res1 = cv2.bitwise_and(imageFrame, imageFrame,mask = mask)
    
    res = cv2.GaussianBlur(res1,(5,5),0)

    edged = cv2.Canny(res, 20, 50)
    #cv2.imshow("edges", edged)
    #cv2.imshow("mask", res)
    cnts, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    out = np.zeros_like (mask)
    cv2.drawContours(imageFrame, [cnts], -1, color = 255, thickness = 2)

    if len(cnts) > 0:

        ((x, y), radius) = cv2.minEnclosingCircle(cnts[0])
        M = cv2.moments(cnts[0])
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius > 5:
            cv2.circle(imageFrame, (int(x), int(y)), int(radius), (255, 255, 255), 2)
            cv2.circle(imageFrame, center, 5, linecolor, -1)

    cv2.imshow("video", imageFrame)

    if x > 320:
        print("\tRight")
        Ser.write(b"R")
    elif x < 280:
        print("\tLeft")
        Ser.write(b"L")
    else: 
        print("\tStraight")
        Ser.write(b"F")
