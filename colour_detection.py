import cv2
import numpy as np
import time

def detect(frame,colour):
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)   

    if(colour=='Brown'):
        brown_lower = np.array([11, 61, 115], np.uint8)
        brown_upper = np.array([31, 81, 195], np.uint8)
        brown_mask = cv2.inRange(hsvFrame, brown_lower, brown_upper)
        if(cv2.countNonZero(brown_mask)>2000):
            return True
        else:
            return False

    elif(colour=='Purple'):
        purple_lower = np.array([115, 127, 215], np.uint8)
        purple_upper = np.array([135, 147, 255], np.uint8)
        purple_mask = cv2.inRange(hsvFrame, purple_lower, purple_upper)
        if(cv2.countNonZero(purple_mask)>2000):
            return True
        else:
            return False

    elif(colour=='Green'):
        green_lower = np.array([64, 146, 161], np.uint8) 
        green_upper = np.array([84, 166, 241], np.uint8)
        green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
        if(cv2.countNonZero(green_mask)>2000):
            return True
        else:
            return False
