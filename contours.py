#!/bin/lib/python

import cv2
import numpy as np


img = cv2.imread('j0.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img_gray,127,255,0)
image,contours,hierarchy = cv2.findContours(thresh, 2, 1)
cnt = contours[0]

# M = cv2.moments(cnt)
# area = cv2.contourArea(cnt)
# perimeter = cv2.arcLength(cnt,True)

# print M,area
#
# cx = int(M['m10']/M['m00'])
# cy = int(M['m01']/M['m00'])
#
# print(cx,cy)

# (x,y),radius = cv2.minEnclosingCircle(cnt)
# center = (int(x),int(y))
# radius = int(radius)
# img = cv2.circle(img,center,radius,(0,255,0),2)

# ellipse = cv2.fitEllipse(cnt)
# img = cv2.ellipse(img,ellipse,(0,255,0),2)

hull = cv2.convexHull(cnt,returnPoints=False)
defects = cv2.convexityDefects(cnt,hull)
# print(len(defects))

for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img,start,end,[0,255,0],2)
    cv2.circle(img,far,5,[0,0,255],-1)

dist = cv2.pointPolygonTest(cnt,(50,50),True)
print(dist)

cv2.namedWindow('img',cv2.WINDOW_KEEPRATIO)
cv2.imshow('img',img)


k = cv2.waitKey(0)
if k == 27:                 # wait for ESC key to exit
    cv2.destroyAllWindows()