import cv2
import numpy as numpy

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
rec = cv2.face.LBPHFaceRecognizer_create()
print(rec.read('trainingData.yml'))
id = 0
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret,img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5);
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        id, conf = rec.predict(gray[y:y+h, x:x+w])
        if id==1:
            cv2.putText(img,"sai",(x,y+h), font, 4,(255,255,255),2,cv2.LINE_AA)
        elif id ==2:
            cv2.putText(img,"giri",(x,y+h), font, 4,(255,255,255),2,cv2.LINE_AA)
        elif id ==3:
            cv2.putText(img,"sashi",(x,y+h), font, 4,(255,255,255),2,cv2.LINE_AA)
        elif id ==4:
            cv2.putText(img,"yaash",(x,y+h), font, 4,(255,255,255),2,cv2.LINE_AA)
        elif id ==5:
            cv2.putText(img,"mam",(x,y+h), font, 4,(255,255,255),2,cv2.LINE_AA)
        elif id ==6:
            cv2.putText(img,"hhh ",(x,y+h), font, 4,(255,255,255),2,cv2.LINE_AA)
        else:
            cv2.putText(img," ",(x,y+h), font, 4,(255,255,255),2,cv2.LINE_AA)
        pass
    cv2.imshow("Faces",img)
    if(cv2.waitKey(1) == ord('q')):
        break
    pass
cam.release()
cv2.destroyAllWindows()
