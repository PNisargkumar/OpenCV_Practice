import cv2

print(cv2.__version__)
flip = 2
goflag =0
def mouseclick(event,x,y,flags,params):
    global x1,x2,y1,y2
    global goflag
    if event == cv2.EVENT_LBUTTONDOWN:
        x1 =x
        y1=y
        goflag = 0
    if event == cv2.EVENT_LBUTTONUP:
        x2=x
        y2=y
        goflag=1
cv2.namedWindow('nanoCam')
cv2.setMouseCallback('nanoCam',mouseclick)
# Uncomment These next Two Line for Pi Camera
# camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# cam= cv2.VideoCapture(camSet)

# Or, if you have a WEB cam, uncomment the next line
# (If it does not work, try setting to '1' instead of '0')
cam = cv2.VideoCapture(0)
dispW = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
dispH = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
while True:
    ret, frame = cam.read()
    if goflag==1:
        cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),3)
        roi=frame[y1:y2,x1:x2]
        cv2.imshow('Copy ROI',roi)
        #cv2.resizeWindow('Copy ROI',x2-x1,y2-y1)
        #cv2.moveWindow('Copy ROI',650,0)
    cv2.imshow('nanoCam', frame)
    cv2.moveWindow('nanoCam',0,0)
    key = cv2.waitKey(1)
    if key % 256 == 27:  # Esc key ==32is spacebar
        break
cam.release()
cv2.destroyAllWindows()