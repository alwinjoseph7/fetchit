import numpy as np
import cv2

video = cv2.VideoCapture("path.mp4")


while(1):
	
	ret, imageFrame = video.read()
	if not ret:
		video=cv2.VideoCapture("path.mp4")
		continue


	hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

	lower = np.array([10, 100, 20], np.uint8)
	upper = np.array([25, 255, 255], np.uint8)
	mask = cv2.inRange(hsvFrame, lower, upper)

	kernal = np.ones((5, 5), "uint8")
	

	mask = cv2.dilate(mask, kernal)
	res = cv2.bitwise_and(imageFrame, imageFrame,
							mask = mask)
	edged = cv2.Canny(res, 1, 1)
	cv2.imshow("edges", edged)
	cv2.imshow("mask", mask)

	contours, hierarchy = cv2.findContours(mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(mask, contours, -1, (0, 255, 0), 3)
	
	
			
	# Program Termination
	cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
	if cv2.waitKey(10) & 0xFF == ord('q'):
		video.release()
		cv2.destroyAllWindows()
		break
