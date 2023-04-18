import cv2
threshold = 0.5
#img = cv2.imread('lena.jpg')
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(3,640)
cam.set(4,480)

classNames = []
classFile = 'coco.names'
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net=cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5,127.5,127.5))
net.setInputSwapRB(True)
while True:
    success, img = cam.read()
    classIds,confs,bbox = net.detect(img,confThreshold=threshold)
    #print(classIds,bbox)
    if len(classIds) != 0:
        for classId , confidence, box in zip(classIds.flatten(),confs.flatten(),bbox):
            cv2.rectangle(img,box,color=(0,255,0),thickness=2)
            cv2.putText(img,classNames[classId -1].upper(),(box[0]+10,box[1]+20),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),1)
            cv2.putText(img,str(round(confidence*100,2)),(box[0]+10,box[1]+40),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),1)


    cv2.imshow('Output',img)
    key = cv2.waitKey(1)
    if key % 256 == 27:  # Esc key ==32is spacebar
        break
cam.release()
cv2.destroyAllWindows()
