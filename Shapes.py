import cv2
import numpy as np

#gives an black frame as per size



#SUDO CODE FOR UNDERSTANDING
#drawing Rectangle
# cv2.rectangle(frame , (startpos), (endPos), (Color), thinkness:int)
#drawing circle
# cv2.circle(frame , (center), radius:int, (Color), thinkness:int)
#drawing line
# cv2.line(frame , (startpos),(endpos),(color),thiskness:int)
#rendering text
# cv2.putText(frame , "text",(startpos),cv2.FONT_HERSHEY_TRIPLEX , Scale:float ,(Color))


def getBlankCanvas(size: list[int])-> np.ndarray:
    height,width = size
    blank_canvas = np.zeros((width,height,3),dtype='uint8')
    return blank_canvas

def getColoredCanvas(size: list[int],color :list[int])-> np.ndarray:
    height,width = size
    colored_canvas = np.zeros((width,height,3),dtype='uint8')
    colored_canvas[:] = color
    return colored_canvas



#useCases of Function provided below

img = getColoredCanvas([400,400],[0,100,0])

cv2.rectangle(img , (100,100),(120,150),(0,0,255),4)
cv2.circle(img,(200,200),50,(200,200,0),5)
cv2.putText(img,"Aman",(10,300),cv2.FONT_HERSHEY_COMPLEX,1.0,(0,255,0))
cv2.imshow("COLOR", img)
#cv2.imshow("BLANK", getBlankCanvas([800,400]))

cv2.waitKey(0)
cv2.destroyAllWindows()

