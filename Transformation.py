import cv2 as cv
import numpy as np

import Resize


def translate(img , x , y):
    tr = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1],img.shape[1])
    return cv.warpAffine(img,tr,dimension)

def rotate(img,angle,rotPoint = None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    rotmat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimesions = (width,height)
    return cv.warpAffine(img,rotmat,dimesions)
    

img = cv.imread("Resources/wall.jpg")
img = Resize.cngScaleFrame(img,0.1)

cv.imshow("DEFAULt",img)

cv.imshow("transform",translate(img,0,-200))
cv.imshow("rota",rotate(img,90))
cv.imshow("flip",cv.flip(img,1))


cv.waitKey(0)


