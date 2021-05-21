import cv2
import numpy as np
import time

video = cv2.VideoCapture(0)

while True:
    _, frame = video.read()
    #frame=cv2.imread("C:\\Users\\adith\\Documents\\Fetch It\\images\\pink.png")
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    brown_lower = np.array([3, 154,  83], np.uint8)
    brown_upper = np.array([23, 174, 163], np.uint8)
    brown_mask = cv2.inRange(hsvFrame, brown_lower, brown_upper)

    purple_lower = np.array([126, 198, 165], np.uint8)
    purple_upper = np.array([146, 218, 245], np.uint8)
    purple_mask = cv2.inRange(hsvFrame, purple_lower, purple_upper)

    pink_lower = np.array([154, 245, 190], np.uint8) 
    pink_upper = np.array([174, 265, 270], np.uint8)
    pink_mask = cv2.inRange(hsvFrame, pink_lower, pink_upper)

    cv2.imshow("original",frame)
    cv2.imshow("purple",purple_mask)
    cv2.imshow("pink",pink_mask)
    cv2.imshow("brown",brown_mask)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        video.release()
        cv2.destroyAllWindows()
        break
    time.sleep(0.1)
