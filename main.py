import cv2
import qr
import colour_detection
import navigate

video = cv2.VideoCapture(0)
colour,start,stop='',False,False

while True:
    _, frame = video.read()
    cv2.imshow("Video",frame)

    if(colour==''):
        colour=qr.read(frame)
        start=True

    elif(start==True and stop==False):
        navigate.nav(frame)
        stop=colour_detection.detect(frame,colour)

    elif(stop==True):
        print("STOP")
        video.release()
        cv2.destroyAllWindows()
        break

    if cv2.waitKey(10) & 0xFF == ord('q'):
        video.release()
        cv2.destroyAllWindows()
        break
