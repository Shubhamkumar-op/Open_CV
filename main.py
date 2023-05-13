import cv2
import numpy as np



# def draw(event,x,y,flags,params):
#   if event == 1:
#     cv2.circle(image,center=(x,y),radius=50, color=(0, 0, 255), thickness=-1)
#
# cv2.namedWindow(winname="window")
# cv2.setMouseCallback("window",draw)
#
# image = cv2.imread('C:/Users/singh/Cv/img/test2.jpg')
# while True:
#   cv2.imshow("window",image)
#   if cv2.waitKey(1) & 0xFF == ord('x'):
#     break
#
# cv2.destroyAllWindows()

###############
# Croping tool
# flag = False
# ix = -1
# iy = -1
#
# def draw(event,x,y,flags,params):
#   global flag,ix,iy
#   if event == 1:
#      flag = True
#      ix = x
#      iy = y
#
#   # if event == 0:
#   #   if flag == True:
#   #     cv2.rectangle(image, pt1=(ix, iy),pt2=(x,y) , color=(0, 0, 0), thickness=1)
#
#
#   elif event == 4:
#     fx = x
#     fy = y
#     flag = False
#     cv2.rectangle(image, pt1=(ix, iy),pt2=(x,y) , color=(0, 0, 0), thickness=1)
#
#     cropped = image[iy:fy,ix:fx]
#     cv2.imshow("new_window",cropped)
#     cv2.waitKey(0)
#
# cv2.namedWindow(winname="window")
# cv2.setMouseCallback("window",draw)
#
# image = cv2.imread('C:/Users/singh/Cv/img/test2.jpg')
# while True:
#   cv2.imshow("window",image)
#   if cv2.waitKey(1) & 0xFF == ord('x'):
#     break
#
# cv2.destroyAllWindows()


#video

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret ,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.imshow("webcame",gray)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows()