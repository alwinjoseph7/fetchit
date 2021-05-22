import cv2
import qr
import colour_detection
import navigate
import time

video = cv2.VideoCapture(0)
colour,stop='',False,

while True:
    _, frame = video.read()
    if(colour==''):
        colour=qr.read(frame) 
    else:
        print("Start:",colour)
        break

time.sleep(3)

while True:
    _, frame = video.read()
    navigate.nav(frame)
    stop=colour_detection.detect(frame,colour)
    
    if(stop==True):
        print("Stop")
        video.release()
        cv2.destroyAllWindows()
        break

    if cv2.waitKey(10) & 0xFF == ord('q'):
        video.release()
        cv2.destroyAllWindows()
        break
