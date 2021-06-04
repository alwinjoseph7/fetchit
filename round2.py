import numpy as np
import cv2
import serial

cap = cv2.VideoCapture(0)
linecolor = (100, 215, 255)
lwr_red = np.array([  9, 206, 142])
upper_red = np.array([ 29, 226 ,222])
lwr_black = np.array([0,0,0], np.uint8)
upper_black = np.array([10,10,40], np.uint8)
lwr_violet = np.array([120,71,53], np.uint8)
upper_violet = np.array([146,166,243], np.uint8)
lwr_pink = np.array([152,86,171], np.uint8)
upper_pink = np.array([183,264,289], np.uint8)
dir = 'n'
pos = 'i'
Ser = serial.Serial("/dev/ttyACM0", baudrate=9600)
Ser.flush()

while True:
    ret, frame = cap.read()
    if not ret:
        _,frame=cap.read()
        
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.inRange(hsv, lwr_red, upper_red)
    mask = cv2.dilate(mask, kernel, iterations=1)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cnts,_=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    center = None
    
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius > 3:
            cv2.circle(frame, (int(x), int(y)), int(radius), (255, 255, 255), 2)
            cv2.circle(frame, center, 3, linecolor, -1)
            
        if(x < 280):
            print("L")
            Ser.write(b"L")

        elif(x > 320):
            print("R")
            Ser.write(b"R")

        else:
            print("F")
            Ser.write(b"F")

    #adding a try block here cuz it wont always detect a qr code every frame, data would be missing variable
    try:
        black_mask = cv2.inRange(hsv, lwr_black, upper_black)
        violet_mask = cv2.inRange(hsv, lwr_violet, upper_violet)
        pink_mask = cv2.inRange(hsv, lwr_pink, upper_pink)
        if(cv2.countNonZero(black_mask)>200):
            print("shift-right")
            dir = 'r'
            pos = 'o'
            #turn 90 degrees clock
        if(cv2.countNonZero(violet_mask)>200):
            print("shift-left")
            dir = 'l'
            pos = 'i'
            #turn 90 degrees anticlock

        if(cv2.countNonZero(pink_mask)>200):
            print("shift-opposite")
            dir = 'o'
                
    except:
        pass

    if(dir == 'r' or 'l'):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.inRange(hsv, lwr_red, upper_red)
        mask = cv2.dilate(mask, kernel, iterations=1)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        cnts,_=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        center = None
        if len(cnts) > 0: #keep robot moving front regardless of len(cnts) value after turning
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            if radius > 2:
                cv2.circle(frame, (int(x), int(y)), int(radius), (255, 255, 255), 2)
                cv2.circle(frame, center, 2, linecolor, -1)
            
            if y > 450:
                #move a bit more then stop
                if(dir == 'r'):
                    #turn 90 degrees anticlock and resume
                    pass
                elif(dir == 'l'):
                    #turn 90 degrees clock and resume
                    pass

    if(dir == 'o'):
        #turn 90 degrees clockwise
        if(pos == 'i'):
            #move some distance and stop
            pass
        elif(pos == 'o'):
            #move some more distance and stop
            pass
        pass
            
                
                

    cv2.imshow("Frame", frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
