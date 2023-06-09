import cv2 as cv
import numpy as np

frameWidth = 640
frameHeight = 480

cap = cv.VideoCapture(0)

def empty(a):
    pass

myColors = [[5,107,0,19,255,255],
           [133,56,0,159,156,255],
           [57,76,0,100,255,255]]
myColorsvalue=[[51,153,255],[255,0,255],[0,255,0]]

def findcolor(frame,mycolors,myColorsvalue):
    imgHSV = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    count = 0
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv.inRange(imgHSV,lower,upper)
        x,y=getContours(mask)
        cv.circle(imgResult,(x,y),10,myColorsvalue[count],cv.FILLED)
        count+=1
        # cv.imshow(str(color[0]),mask)

def getContours(frame):
    # The contours are stored in the contours variable, and the hierarchy of the contours is stored in the hierarchy variable
    contours,hierarchy = cv.findContours(frame,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        # This line calculates the area of the current contour using the cv.contourArea
        area = cv.contourArea(cnt)
        if area>500:
            # cv.drawContours(imgResult,cnt,-1,(0,0,255),2)
            # This line calculates the perimeter of the contour using the cv.arcLength function and stores it in the peri variable.
            peri = cv.arcLength(cnt,True)
            # This line approximates the contour shape with a simpler polygon using the cv.approxPolyDP function.
            approx = cv.approxPolyDP(cnt,0.02*peri,True)
            x,y,z,w = cv.boundingRect(approx)
    return x+w//2,y

cap = cv.VideoCapture(0)
cap.set(3,400)
cap.set(4,400)
cap.set(10,150)
while True:
    ret ,frame = cap.read()
    imgResult = frame.copy()
    findcolor(frame,myColors,myColorsvalue)
    # gray = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    cv.imshow("webcame",imgResult)

    if cv.waitKey(1) & 0xFF == ord('x'):
        break
cv.destroyAllWindows()