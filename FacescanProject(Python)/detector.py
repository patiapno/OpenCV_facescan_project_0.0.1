import cv2,os
import numpy as np


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "Classifiers/face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path = 'dataSet'

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, im =cam.read()

    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.2,5)

    for(x,y,w,h) in faces:

        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)
        nbr_predicted,conf = recognizer.predict(gray[y:y+h,x:x+w])

        if(nbr_predicted==14):
             nbr_predicted='pume'
        elif(nbr_predicted==2):
             nbr_predicted='Anirban'

        cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
        cv2.putText(im, (nbr_predicted), (x,y-40), font, 2, (255,255,255), 3)
        cv2.imshow('im',im)
        cv2.waitKey(10)









