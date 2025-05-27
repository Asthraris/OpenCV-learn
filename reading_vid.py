import cv2 as cv

#my modules
from Resize import getFrameDuration

#template jesa bana le

# source = "Resources/car.mp4"
source = 0


#webcam ke liye 0 bola hai , 0 is primaty cam 1 is not available for laptop
vid = cv.VideoCapture(source)


#time after which frame are switch
flipDuration :int
if isinstance(source,str) :# means local video #isinstance checks the datatype and returns boolean
    flipDuration = getFrameDuration(vid)
else:
    flipDuration = 1
    
#iterate over entire frames of vidio
while True:
    #reads one frame then inc the frame ptr to read next automatically
    # returns success rate bool , and frame data
    frameSuccess,frame = vid.read()
    if not frameSuccess:
        break
    # imshow mutliple times windows create nhi karta woh name se bas videos ko switch karta hai so names are importnat

    #filters
    # frame = cv.GaussianBlur(frame,(11,11),cv.BORDER_DEFAULT)
    # frame = 1-cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    # frame = cv.Canny(frame,80,80)
    cv.imshow("Video",cv.flip(frame , 1))

    

    # wait for one sec then loop again while loop or accept q key to quit
    # 0->stop of next key
    # 10++ ->slowMotion
    #webacam me agar 0 rakhte hai tab moment capture hote hai ;]
    #abhi me tukke ka kaam kar raha hu there is no way to play video in same fps as it was rrecoredr
    if cv.waitKey(flipDuration) & 0xFF==ord('q'):
        break

#only for Video cache mese buffer ko realese karna padta hai
vid.release()
cv.destroyAllWindows()