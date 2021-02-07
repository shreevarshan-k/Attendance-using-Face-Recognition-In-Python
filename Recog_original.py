import cv2
from PIL import Image
import numpy
import pyttsx3
import xlwrite
import time
import sys
start=time.time()

period=8




engine = pyttsx3.init()

load = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


cap=cv2.VideoCapture(0)

rec = cv2.face.LBPHFaceRecognizer_create()

rec.read("recognizer/TraningData.yml")
id=0;
filename='filename'
dict = {
            'item1': 1
}

font = cv2.FONT_HERSHEY_SIMPLEX


f = open("datatext.txt","r")
user = {}
for x  in f:
        y,z = x.split(" ")
        user[y] = z.replace("\n","")

while True:
    status,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = load.detectMultiScale(gray,1.3,5)
    eyes = load.detectMultiScale(gray,1.3,5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        id,conf = rec.predict(gray[y:y+h,x:x+w])
        
       
        
        
       
                        
        if(conf>75):
            name = "Unknown"
            
        else:
             if(id==1089):
                id='shree'
                if((str(id)) not in dict):
                        filename=xlwrite.output('attendance','class1',1,id,'yes');
                        dict[str(id)]=str(id);
                
             elif(id==1234):
                      id = 'anu'
                      if ((str(id)) not in dict):
                              filename =xlwrite.output('attendance', 'class1', 2, id, 'yes');
                              dict[str(id)] = str(id);
             else:
                     id = 'Unknown, can not recognize'
                     flag=flag+1
                     break
        
        cv2.putText(img,str(id), (x,y),cv2.FONT_HERSHEY_SIMPLEX, 1, 255)

        
    cv2.imshow('FaceDetect',img)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        
            
        break;
    if time.time()>start+period:
        break;
print("Attendance Marked for",id)


cap.release()
cv2.destroyAllWindows()
    
















    
