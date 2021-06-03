import numpy as np
import cv2

cap = cv2.VideoCapture(0)
linecolor = (100, 215, 255)
lwr_red = np.array([14, 74, 66])
upper_red = np.array([48, 189, 255])

while True:
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.inRange(hsv, lwr_red, upper_red)
    mask = cv2.dilate(mask, kernel, iterations=1)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cnts,_=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    center = None
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius > 5:
            cv2.circle(frame, (int(x), int(y)), int(radius), (255, 255, 255), 2)
            cv2.circle(frame, center, 5, linecolor, -1)
    #print((x,y))

    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    cv2.imshow("Frame", frame)

    if(x < 280):
        print("L")

    elif(x > 320):
        print("R")

    else:
        print("F")





