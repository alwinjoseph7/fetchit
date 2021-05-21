import cv2
import numpy as np
import time

video = cv2.VideoCapture(0)

while True:
    _, frame = video.read()

    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    pink_lower = np.array([10, 151, 71], np.uint8)
    pink_upper = np.array([30, 171, 151], np.uint8)
    pink_mask = cv2.inRange(hsvFrame, pink_lower, pink_upper)

    purple_lower = np.array([111, 123, 215], np.uint8)
    purple_upper = np.array([131, 143, 295], np.uint8)
    purple_mask = cv2.inRange(hsvFrame, purple_lower, purple_upper)

    brown_lower = np.array([144, 146, 178], np.uint8)
    brown_upper = np.array([164, 166, 258], np.uint8)
    brown_mask = cv2.inRange(hsvFrame, brown_lower, brown_upper)

    cv2.imshow("original",frame)
    cv2.imshow("pink",pink_mask)
    cv2.imshow("purple",purple_mask)
    cv2.imshow("brown",brown_mask)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        video.release()
        cv2.destroyAllWindows()
        break
    time.sleep(0.1)
