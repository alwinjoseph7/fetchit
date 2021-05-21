import cv2
import numpy as np
import time

video = cv2.VideoCapture(0)

while True:
    _, frame = video.read()
    #frame=cv2.imread("C:\\Users\\adith\\Documents\\Fetch It\\images\\purple.png")
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    brown_lower = np.array([3, 154,  83], np.uint8)
    brown_upper = np.array([23, 174, 163], np.uint8)
    brown_mask = cv2.inRange(hsvFrame, brown_lower, brown_upper)

    purple_lower = np.array([100,  70, 130], np.uint8)
    purple_upper = np.array([140,  100, 222], np.uint8)
    purple_mask = cv2.inRange(hsvFrame, purple_lower, purple_upper)

    green_lower = np.array([30, 70, 130], np.uint8) 
    green_upper = np.array([70, 100, 255], np.uint8)
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

    cv2.imshow("original",frame)
    cv2.imshow("purple",purple_mask)
    cv2.imshow("green",green_mask)
    cv2.imshow("brown",brown_mask)

    if(cv2.countNonZero(green_mask)>2000 or cv2.countNonZero(purple_mask)>2000 or cv2.countNonZero(purple_mask)>2000):
        print("Stop")
        break
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        video.release()
        cv2.destroyAllWindows()
        break
