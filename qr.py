import cv2
import numpy as np

video = cv2.VideoCapture(0)
while True:
    _, frame = video.read()
    data,_,_=cv2.QRCodeDetector().detectAndDecode(frame)
    if(data!=''):
        print(data)
        video.release()
        break

