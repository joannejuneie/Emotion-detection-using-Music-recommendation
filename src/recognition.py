from tkinter import Image
import cv2
from cv2 import CAP_DSHOW
from cv2 import CAP_ANDROID
from cv2 import CAP_GPHOTO2
from cv2 import CAP_FFMPEG
from cv2 import CAP_IMAGES
from cv2 import CAP_OPENCV_MJPEG
from cv2 import CAP_VFW
import PIL.Image
import numpy as np
import os 


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("src/trainer/trainer.yml")
cascadePath = "src/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

# Emotions related to ids: example ==> Anger: id=0,  etc
names = ['Happy', 'Sad'] 

# Initialize and start realtime video capture
print("1")
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height
print("2")
# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
while(True):
    ret, img =cam.read()
    cv2.imshow('Emotion Detector', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.imwrite("src/plainpic.jpg",img)    
#pic=file_select()
print("3")
#img = cv2.imread(pic)
#img = cv2.flip(img, -1) # Flip vertically
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale( 
    gray,
    scaleFactor = 1.2,
    minNeighbors = 5,
    minSize = (int(minW), int(minH)),
    )
for(x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

    id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

    # Check if confidence is less them 100 ==> "0" is perfect match 
    if (confidence < 100):
        id = names[id]
        confidence = "  {0}%".format(round(100 - confidence))
    else:
        id = "unknown"
        confidence = "  {0}%".format(round(100 - confidence))
    
    cv2.putText(img, str(id), (x+5,y+15), font, 1, (255,255,255), 2)
f = open("result.txt", "w")
f.write(str(id))
f.close()
# fp = open('C:/Users/Dell/Desktop/emotion/Emotion_detection/src/happy.jpg',"rb")
# image = PIL.Image.open(fp)
# image = Image.open('C:/Users/Dell/Desktop/emotion/Emotion_detection/srchappy.jpg')
# if str(id)=="Happy":
#     cv2.imwrite("src/emotion_pic.jpg",image)

cv2.imwrite("src/generated_pic.jpg",img) 

print("\n [INFO] Done detecting and Image is saved")
cam.release()
cv2.destroyAllWindows()
