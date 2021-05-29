import cv2
import numpy as np
pixel = (20,60,80) 
cap = cv2.VideoCapture(0)

def pick_color(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = image_hsv[y,x]
        upper =  np.array([pixel[0] + 10, pixel[1] + 10, pixel[2] + 40])
        lower =  np.array([pixel[0] - 10, pixel[1] - 10, pixel[2] - 40])
        print(pixel, lower, upper)
        image_mask = cv2.inRange(image_hsv,lower,upper)
        cv2.imshow("mask",image_mask)
def main():
    import sys
    global image_hsv, pixel
    kj,image_src=cap.read()
    #image_src=cv2.imread("C:\\Users\\adith\\Documents\\Fetch It\\resources\\end.png")
    image=cv2.GaussianBlur(image_src,(93,93),0)
    cv2.imshow("bgr",image_src)
    cv2.namedWindow('hsv')
    cv2.setMouseCallback('hsv', pick_color)
    # now click into the hsv img , and look at values:
    image_hsv = cv2.cvtColor(image_src,cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv",image_hsv)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
main()