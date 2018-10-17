import cv2
import numpy as np

#Load the classifier
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Add video capture object
cap=cv2.VideoCapture(0)

#Lets test the camera now
ret,img=cap.read()
#cv2.imshow('Akshay',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#Before using the face detector we need comvert the captured image to Gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Now lets apply the face detector to detect faces in our captured image
faces = detector.detectMultiScale(gray, 1.3, 5)


#the above line will get the x,y and height,width of all the faces present in the captured image in a list, So now we have to loop through all the faces and draw rectangle there
#for (x,y,w,h) in faces:
#    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)


print faces
#cv2.imshow('frame',img)
for (x,y,w,h) in faces:
    cv2.imshow('frame',cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2))
    cv2.waitKey(0)
    cap.release()
    cv2.destroyAllWindows()


