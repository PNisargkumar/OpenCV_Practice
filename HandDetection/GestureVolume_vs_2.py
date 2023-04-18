import cv2
import HandTrackingModule as htm
import time
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np
####################################
wCam, hCam = 640, 480
####################################
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(3, wCam)
cam.set(4, hCam)
pTime = 0
cTime = 0

detector = htm.handDetector(detectionCon = 0.7)
# pycow   Windows volume control

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volrange = volume.GetVolumeRange()
minvol = volrange[0]
maxvol = volrange[1]
# vol = volume.GetMasterVolumeLevel()
# length = np.interp(vol, [-65.5, 0], [400, 150])
# volBar = np.interp(length, [15, 160], [400, 150])


while True:
    success, img = cam.read()
    # find hand
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        # filter based on size

        # Find Distance between index and Thumb

        # Convert volume
        # Reduce Resolution to make it smoother
        # Check fingers up and set volume
        # drawings
        # frame rate

        # print(lmList[4],lmList[8])
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2,y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (cx,cy), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)

        length = math.hypot(x2-x1,y2-y1)
        #  hand range = 15 - 160
        #  Volume range = -65.5 - 0

        vol = np.interp(length, [15, 160], [minvol, maxvol])
        volume.SetMasterVolumeLevel(vol, None)
        # print(length,vol)
        if length < 30:
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
        cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
        volBar = np.interp(length, [15, 160], [400, 150])
        cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
        # disp percentage
        volPer = np.interp(length, [15, 160], [0, 100])
        cv2.putText(img, f'{int(volPer)}%', (40, 450), cv2.FONT_HERSHEY_PLAIN,
                    2, (0, 250, 0), 1)

    # fps
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 25), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 1)
    # disp Image
    cv2.imshow('Image', img)
    # cv2.moveWindow('Image', 0, 0)
    key = cv2.waitKey(1)
    if key % 256 == 27:  # Esc if key ==32 is spacebar
        break
cam.release()
cv2.destroyAllWindows()