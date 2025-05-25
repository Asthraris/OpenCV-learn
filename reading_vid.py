import cv2 as cv
from Resize import cngScaleFrame , cngResolutionFrame

source : str= "Resources/car.mp4"

#webcam ke liye 0 bola hai , 0 is primaty cam 1 is not available for laptop
rain_vid = cv.VideoCapture(source)



rain_vid = cngResolutionFrame(rain_vid , 720,720)

#iterate over entire frames of vidio
while True:
    #reads one frame then inc the frame ptr to read next automatically
    # returns success rate bool , and frame data
    frameSuccess,frame = rain_vid.read()
    if not frameSuccess:
        break
    # imshow mutliple times windows create nhi karta woh name se bas videos ko switch karta hai so names are importnat
    cv.imshow("Video",cngScaleFrame(frame , 0.5))

    # wait for one sec then loop again while loop or accept q key to quit
    # 0->stop of next key
    # 10++ ->slowMotion


    #webacam me agar 0 rakhte hai tab moment capture hote hai ;]
    #abhi me tukke ka kaam kar raha hu there is no way to play video in same fps as it was rrecoredr
    if cv.waitKey(duration) & 0xFF==ord('q'):
        break

#only for Video cache mese buffer ko realese karna padta hai
rain_vid.release()
cv.destroyAllWindows()