import cv2
import numpy as np
import time

video = cv2.VideoCapture(0)
colours=[['pink',255, 192, 203],['purple',128,0,128],['brown',165,42,42]]

def get_color_name(R, G, B):
    min = 10000
    for N,r,g,b in colours:
        d = abs(R - r) + abs(G- g) + abs(B - b)
        if d <= min:
            min = d
            cname = N
    return cname

while True:
    _, frame = video.read()

    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

    green_lower = np.array([25, 52, 72], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

    blue_lower = np.array([94, 80, 2], np.uint8)
    blue_upper = np.array([120, 255, 255], np.uint8)
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

    cv2.imshow("original",frame)
    cv2.imshow("red",red_mask)
    cv2.imshow("green",green_mask)
    cv2.imshow("blue",blue_mask)

    r = int(cv2.countNonZero(red_mask)/(frame.size/3)*255)
    g = int(cv2.countNonZero(green_mask)/(frame.size/3)*255)
    b = int(cv2.countNonZero(blue_mask)/(frame.size/3)*255)

    print(r," ",g," ",b)
    print(get_color_name(r,g,b))
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        video.release()
        cv2.destroyAllWindows()
        break
    time.sleep(0.1)
