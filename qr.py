import cv2
import numpy as np

def read(frame):
    data,_,_=cv2.QRCodeDetector().detectAndDecode(frame)
    if(data!=''):
        colour=data.split(":")[1]
        return colour
    else:   
        return ''