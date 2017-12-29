import cv2
import os
import numpy as np
import faceServerlib as faceserv
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')

cascdePath = "Classifiers/face.xml"
faceCascade = cv2.CascadeClassifier(cascdePath)


font = cv2.FONT_HERSHEY_SIMPLEX

cam = cv2.VideoCapture(0)
path = 'dataSet'

while True:
    ret, im =cam.read()
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3,5)
    for(x,y,w,h) in faces:

        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,225,0), 4)

        conf,Id = recognizer.predict(gray[y:y+h,x:x+w])

        print(conf)
        findout = faceserv.insertData(str(conf))

        cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,225,0), -1)
        cv2.putText(im, findout, (x,y-40), font, 2, (255,255,255), 3)

    cv2.imshow('im',im)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    
can.release()
cv2.destroyAllWindows()
