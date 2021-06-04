import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(False, 1, 0.75, 0.5)
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    flag = 0
    if results.multi_hand_landmarks:
        myHand = results.multi_hand_landmarks[0]
        for id, lm in enumerate(myHand.landmark):
            flag = 1

    if flag == 1:
        print("detected")
        
    cv2.imshow("hand", img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        cap.release()
        break