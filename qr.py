import cv2
import numpy as np

def read():
    video = cv2.VideoCapture(0)
    while True:
        _, frame = video.read()
        data,_,_=cv2.QRCodeDetector().detectAndDecode(frame)
        if(data!=''):
            colour=data.split(":")[1]
            video.release()
            break
    return colour

