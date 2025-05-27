import cv2 as cv



img = cv.imread("Resources/wall.jpg")


# openCV takes BGR value not normally rgb value

# frame = cv.cvtColor(frame , cv.COLOR_<attribs>)
#   cv.COLOR_BGR2RGB -> inverts red channel with blue
#   cv.COLOR_BGR2GRAY -> GreyScale black and white

# Blur 
#   frame = cv.GaussianBlur(frame,(Intensity_x,intensity_y),cv.BORDER_<attribs>)
        #always use odd kernal values in intensity or error
        #no significant change or visible in BORDER_DEFUALT else.

#canny Lines
#   frame = cv.Canny(frame ,(<intensity to detect>,<intensity to detect>))
        #more the intesity less it will check for detail
        #i can also achieve this using gaussian blur then canny lines to regulate intensity
    #Dilating Image
        #increasing effect of canny image thick lines
            #iso = cv.dilate(iso,(10,10),iterations=4)
    #Eroding image
        #dec thickness of canny effect
            #iso = cv.erode(iso,(3,3),iterations=1)

#image Resizing


img = img[200:200,300:300]

cv.imshow("hello",img)

cv.waitKey(0)