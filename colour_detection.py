import cv2
import numpy as np
import time

def detect(frame,colour):
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)   

    if(colour=='Brown'):
        brown_lower = np.array([11, 61, 115], np.uint8)
        brown_upper = np.array([31, 81, 195], np.uint8)
        brown_mask = cv2.inRange(hsvFrame, brown_lower, brown_upper)
        if(cv2.countNonZero(brown_mask)>200):
            return True
        else:
            return False

    elif(colour=='Pink'):
        pink_lower = np.array([162, 143, 135], np.uint8)
        pink_upper = np.array([182, 163, 215], np.uint8)
        pink_mask = cv2.inRange(hsvFrame, pink_lower, pink_upper)
        if(cv2.countNonZero(pink_mask)>200):
            return True
        else:
            return False

    elif(colour=='Green'):
        green_lower = np.array([64, 146, 161], np.uint8) 
        green_upper = np.array([84, 166, 241], np.uint8)
        green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
        if(cv2.countNonZero(green_mask)>200):
            return True
        else:
            return False
