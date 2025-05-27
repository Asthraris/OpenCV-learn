import cv2 as cv
import Resize 
img = Resize.cngScaleFrame((cv.imread("Resources/wall.jpg")),0.1)

can = cv.Canny(cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT) ,125,125)


cv.imshow("def",img)
cv.imshow("canny",can)
contours,hiearchy = cv.findContours(can,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(len(contours))

cv.waitKey(0)