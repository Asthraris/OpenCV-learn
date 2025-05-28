import cv2


cascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

def detect(frame):
    face_rect = cascade.detectMultiScale(frame,scaleFactor= 1.3,minNeighbors= 5)
    for(x,y,w,h)in face_rect:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    return frame

    