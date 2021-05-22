import cv2
import qr
import colour_detection
import navigate
import time

video = cv2.VideoCapture("resources\\pathfinal.mp4")
colour,stop='',False,

while True:
    _, frame = video.read()
    if(colour==''):
        colour=qr.read(frame) 
    else:
        print("\n\n--------------Start:",colour,"--------------\n\n")
        break

time.sleep(3)

while True:
    _, frame = video.read()
    
    try:
        navigate.nav(frame)
    except:
        print("Track Not Visible")

    stop=colour_detection.detect(frame,colour)
    
    if(stop==True):
        print("\n\n--------------Stop--------------\n\n")
        video.release()
        cv2.destroyAllWindows()
        break

    if cv2.waitKey(10) & 0xFF == ord('q'):
        video.release()
        cv2.destroyAllWindows()
        break
