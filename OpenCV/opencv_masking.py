import cv2

# print(cv2.__version__)
flip = 2
cv2.namedWindow('nanoCam',cv2.WINDOW_NORMAL)
cvlogo = cv2.imread('opencvlogo.png')

# Uncomment These next Two Line for Pi Camera
# camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# cam= cv2.VideoCapture(camSet)

# Or, if you have a WEB cam, uncomment the next line
# (If it does not work, try setting to '1' instead of '0')
cam = cv2.VideoCapture(0)
dispW = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
dispH = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
cvlogo = cv2.resize(cvlogo, (dispW, dispH))
cvlogogray=cv2.cvtColor(cvlogo,cv2.COLOR_BGR2GRAY)

_,bgmask=cv2.threshold(cvlogogray,225,255,cv2.THRESH_BINARY)
fgmask=cv2.bitwise_not(bgmask)
fg=cv2.bitwise_and(cvlogo,cvlogo,mask=fgmask)
#cv2.imshow('OPENCV LOGO',cvlogo)
#cv2.moveWindow('OPENCV LOGO',650,0)
#cv2.imshow('MASK',bgmask)
#cv2.moveWindow('MASK',1300,0)
#cv2.imshow('FG',fg)
#cv2.moveWindow('FG',650,500)
print(dispW,dispH)
while True:
    ret, frame = cam.read()
    #frame=cv2.resize(frame, (320, 240))


    cv2.imshow('nanoCam', frame)
    cv2.moveWindow('nanoCam', 0, 0)
    bg = cv2.bitwise_and(frame, frame, mask=bgmask)
    compimg = cv2.add(bg,fg)
    #cv2.imshow('compimg', compimg)
    #cv2.moveWindow('compimg', 0, 500)
    blended=cv2.addWeighted(frame,.90,cvlogo,.1,0)
    #cv2.imshow('blended', blended)
    #cv2.moveWindow('blended', 650, 0)
    fg2=cv2.bitwise_and(blended,blended,mask=fgmask)
    #cv2.imshow('blended', blended)
    #cv2.moveWindow('blended', 650, 500)
    compfinal =cv2.add(bg,fg2)
    cv2.imshow('compimgfinal', compfinal)
    cv2.moveWindow('compimgfinal', 0, 500)
    key = cv2.waitKey(1)
    if key % 256 == 27:  # Esc key ==32is spacebar
        break
cam.release()
cv2.destroyAllWindows()