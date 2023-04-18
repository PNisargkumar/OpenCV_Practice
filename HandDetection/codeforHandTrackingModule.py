import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

pTime = 0
cTime = 0
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
detector = htm.handDetector()
while True:
    success, img = cam.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw= False)
    # if len(lmList) != 0:
    #     print(lmList[5])
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0))
    cv2.imshow('Image', img)
    cv2.moveWindow('Image', 0, 0)
    key = cv2.waitKey(1)
    if key % 256 == 27:  # Esc key ==32is spacebar
        break
cam.release()
cv2.destroyAllWindows()