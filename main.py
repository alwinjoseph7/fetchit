import cv2
import qr
import colour_detection
import pathfollow
import time
import serial

video = cv2.VideoCapture(0)
colour,stop='',False,
Ser = serial.Serial("/dev/ttyACM0", baudrate=9600)
Ser.flush()

while True:    
    flag, frame = video.read()
    if not flag:
        _, frame = video.read()
    
    try:
        d=pathfollow.nav(frame)
        Ser.write(bytes(d,'utf-8'))
    except:
        print("Track Not Visible")
        if Ser.inWaiting>0:
            Ser.write(b"s")
            #Ser.write(b"x")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        video.release()
        cv2.destroyAllWindows()
        break