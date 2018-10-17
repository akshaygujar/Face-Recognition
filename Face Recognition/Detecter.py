import cv2
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create();
recognizer.read('Trainner/trainner.yml')

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);


cam = cv2.VideoCapture(0)
#font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)

fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 2
fontcolor = (0, 0, 255)
while True:
    Id1 = ""
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        print str(Id)
        if(conf<5s0):
            if(Id==103052):
                Id1 = "Akshay"
                #cv2.putText(im, "Akshay", (x,y+h), fontface, fontscale, fontcolor)
            elif(Id==110968):
                Id1 = "Devender"
                #cv2.putText(im, "Devender", (x,y+h), fontface, fontscale, fontcolor)
            elif(Id==90092):
                Id = "Suresh"
                #cv2.putText(im, "Suresh", (x,y+h), fontface, fontscale, fontcolor)
            elif(Id==118667):
                Id1 = "Jayshree"
                #cv2.putText(im, "Jayshree", (x,y+h), fontface, fontscale, fontcolor)
        else:
            Id1 = "?"
            #cv2.putText(im, "Unknown", (x,y+h), fontface, fontscale, fontcolor)
        
        
        cv2.putText(im, str(Id), (x,y+h), fontface, fontscale, fontcolor)
        
    cv2.imshow('Video Stramming Face Recognition',im) 
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
