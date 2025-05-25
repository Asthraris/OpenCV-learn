import cv2 as cv

#this way i can create moduules for python functions 

#Stored Video ke liye ese resolution change kar sakte hai
def cngScaleFrame(frame , scale = 0.5):
    #is [0] se mujhe lagta hai ki opencv bhi 0,0 cordinate image inversion use karta hai as opengl does
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimes = (width,height)
    return cv.resize(frame ,dimes, interpolation=cv.INTER_AREA)


#only for live video NOT FOR STORED VIDEO
def cngResolutionFrame(Video ,width,height ):
    # OpenCv has 3,4 as width and height
    Video.set(3,width)
    Video.set(4,height)
    return Video

#concrete way to find fps and play real duration [[ONLY FOR PRE RECOREDED VIDEOS IN WEBCAM IT WILL GIVE ERROR]]
def getFrameDuration(Video):
    fps = Video.get(cv.CAP_PROP_FPS)
    frame_count = Video.get(cv.CAP_PROP_FRAME_COUNT)
    duration :int  = (int)(frame_count/fps)
    return duration
