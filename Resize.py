import cv2 as cv

#this way i can create moduules for python functions 





#same will have same RATIO in scale
def cngScaleFrame(frame , scale = 0.5):
    #is [0] se mujhe lagta hai ki opencv bhi 0,0 cordinate image inversion use karta hai as opengl does
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimes = (width,height)
    return cv.resize(frame ,dimes, interpolation=cv.INTER_AREA)


#for UNeven resolution frame
def cngResolutionFrame(frame , Dimension):
    return cv.resize(frame,Dimension,interpolation=cv.INTER_AREA)

def EnlargeFrame(frame , Dimension):
    return cv.resize(frame,Dimension,interpolation=cv.INTER_LINEAR)

#concrete way to find fps and play real duration [[ONLY FOR PRE RECOREDED VIDEOS IN WEBCAM IT WILL GIVE ERROR]]
def getFrameDuration(Video : cv.VideoCapture):
    fps = Video.get(cv.CAP_PROP_FPS)
    frame_count = Video.get(cv.CAP_PROP_FRAME_COUNT)
    duration :int  = (int)(frame_count/fps)
    return duration
