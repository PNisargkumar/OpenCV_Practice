import cv2
import numpy as np
#print(cv2.__version__)
flip = 2
cv2.namedWindow('nonoCam')
# Uncomment These next Two Line for Pi Camera
# camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# cam= cv2.VideoCapture(camSet)

# Or, if you have a WEB cam, uncomment the next line
# (If it does not work, try setting to '1' instead of '0')
cam = cv2.VideoCapture(0)
dispW = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
dispH = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
img1 = np.zeros((dispH,dispW,1),np.uint8)
img1[0:480,0:320]=[255]
img2 = np.zeros((dispH,dispW,1),np.uint8)
img2[190:290,270:375]=[255]
bit=cv2.bitwise_xor(img1,img2)
print(dispW,dispH)
while True:
    ret, frame = cam.read()


    cv2.imshow('img1', img1)
    cv2.moveWindow('img1', 0,520)
    cv2.imshow('img2', img2)
    cv2.moveWindow('img2', 655,520)
    cv2.imshow('and', bit)
    cv2.moveWindow('and', 655,0)
    frame=cv2.bitwise_and(frame,frame,mask=bit)
    cv2.imshow('nanoCam', frame)
    cv2.moveWindow('nanoCam', 0, 0)
    key = cv2.waitKey(1)
    if key % 256 == 27:  # Esc key ==32is spacebar
        break
cam.release()
cv2.destroyAllWindows()