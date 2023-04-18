import cv2
import random

# print(cv2.__version__)
#dispW = 640
#dispH = 480
flip = 2
# Uncomment These next Two Line for Pi Camera
# camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# cam= cv2.VideoCapture(camSet)

# Or, if you have a WEB cam, uncomment the next line
# (If it does not work, try setting to '1' instead of '0')
cam = cv2.VideoCapture(0)
dispW = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
dispH = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
bw=int(dispW*.2)
bh=int(dispH*.2)
xpos=int(random.randint(0,dispW-bw))
ypos=int(random.randint(0,dispH-bh))
dx=3
dy=3
while True:
    ret, frame = cam.read()
    roi = frame[ypos:ypos+bh,xpos:xpos+bw].copy()   #create a copy not refrence to original
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    frame[ypos:ypos+bh,xpos:xpos+bw] = roi
    cv2.rectangle(frame,(xpos,ypos),(xpos+bw,ypos+bh),(255,0,0),3)
    if xpos < 0 or xpos + bw > dispW:
        dx = dx * -1
    if ypos < 0 or ypos + bh > dispH:
        dy = dy * -1
    xpos = xpos+dx
    ypos = ypos+dy
    cv2.imshow('nanoCam', frame)
    cv2.moveWindow('nanoCam',0,0)
    key = cv2.waitKey(1)
    if key%256 == 27:
        break
cam.release()
cv2.destroyAllWindows()