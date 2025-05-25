import cv2 as cv
#python executable file nhi batnata hai ye interprete karke show karta hai hence we get no static exe file after compiling by python main.py
#i can use pyinstaller later for static app

from Resize import cngScaleFrame


    


ske_img = cv.imread("Resources/Skeleton.jpg")
#creates the window using below command new window for new command
#it uses win32 api for windows , Qt for linus and Mac
cv.imshow("DEMO", cngScaleFrame(ske_img , 0.25))
#keeps the window open till any key is pressed
cv.waitKey(0)

cv.destroyAllWindows()
