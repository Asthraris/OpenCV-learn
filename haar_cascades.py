import cv2 as cv
#creating face detecter

img = cv.imread("Resources/skeleton.jpg")

grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
# point to notice that it will not detect if the face is titled or any little side profile its only good of front face in good lightimng offcource

#1.3 is strength or accuracy to detect 
#- scaleFactor (1.3 in your case): This parameter controls how much the image size is reduced at each image scale. A value of 1.3 means the image is scaled down by 30% at each step, helping detect objects of different sizes. A lower value (e.g., 1.05) makes detection more precise but slower, while a higher value speeds up detection but may miss some objects.
#- minNeighbors (5 in your case): This parameter defines how many neighboring rectangles a candidate detection must have to be considered valid. A higher value (e.g., 5) ensures fewer false positives but may miss some objects, while a lower value increases detections but may include more false positives.
faces_rectangle = haar_cascade.detectMultiScale(img,scaleFactor=1.3,minNeighbors=5)
#this will retrun points tht which it will detect face if ther are mopre than one no. of faces it gicve give arr of that struct

#util for this is made in face_detect
for(x,y,w,h) in faces_rectangle:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),thickness=2)

cv.imshow("face",cv.resize(img,(720,480)))
cv.waitKey(0)

