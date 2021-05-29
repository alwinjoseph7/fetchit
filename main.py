import cv2
import qr
import colour_detection
import navigate
import time
import serial

video = cv2.VideoCapture(0)
colour,stop='',False,
Ser = serial.Serial("/dev/ACM0", baudrate=9600)
Ser.flush()

while True:
    flag, frame = video.read()
    if not flag:
        _, frame = video.read()
    cv2.imshow("QR",frame)   
    
    print("\n\n--------------Waiting for QR Code--------------\n\n")
    if(colour==''):
        colour=qr.read(frame) 
    else:
        print("\n\n--------------Start:",colour,"--------------\n\n")
        print("--------------Please Remove the QR code--------------")
        cv2.destroyWindow("QR")
        break

    if cv2.waitKey(10) & 0xFF == ord('q'):
        video.release()
        cv2.destroyAllWindows()
        break

time.sleep(1)
#rotate in place

while True:    
    flag, frame = video.read()
    if not flag:
        _, frame = video.read()
    
    try:
        d=navigate.nav(frame)
        Ser.write(str(d))
    except:
        print("Track Not Visible")
        if Ser.inWaiting>0:
            Ser.write(b"S")
            #FailSafe
        
    stop=colour_detection.detect(frame,colour)
    
    if(stop==True):
        print("\n\n--------------Stop--------------\n\n")
        if Ser.inWaiting>0:
            Ser.write(b"S")
        video.release()
        cv2.destroyAllWindows()
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        video.release()
        cv2.destroyAllWindows()
        break
