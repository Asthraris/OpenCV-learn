import cv2 as cv
import numpy as np
import Resize 
img = Resize.cngScaleFrame((cv.imread("Resources/wall.jpg")),0.1)

can = cv.Canny(cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT) ,125,125)
blank = np.zeros(img.shape,dtype="uint8")

cv.imshow("def",img)
cv.imshow("canny",can)
contours,hiearchy = cv.findContours(can,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)

#leaves the lesser value as black andstaurates the higher value
ret,thres = cv.threshold(img,100,255,cv.THRESH_BINARY)
cv.imshow("thrashed",thres)

dr = cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow("Drawed",dr)

cv.waitKey(0)