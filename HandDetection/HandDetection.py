import cv2
import mediapipe as mp
import time

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw= mp.solutions.drawing_utils

pTime =0
cTime =0

while True:
    success, img = cam.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLns in results.multi_hand_landmarks:
            for id,lm in enumerate(handLns.landmark):
                # print(id,lm)
                h,w,c =img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)
                #print(id, cx,cy)


                mpDraw.draw_landmarks(img,handLns,mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0))

    cv2.imshow('Image', img)
    cv2.moveWindow('Image', 0, 0)
    key = cv2.waitKey(1)
    if key % 256 == 27:  # Esc key ==32is spacebar
        break
cam.release()
cv2.destroyAllWindows()


