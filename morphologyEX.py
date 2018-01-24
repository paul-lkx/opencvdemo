#!/bin/lib/python

import cv2
import numpy as np

img = cv2.imread('j0.jpg',0)
# img = cv2.imread('j1.jpg',0) # "j2.jpg" or "j1.jpg"

# kernel = np.ones((5,5),np.uint8)
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

erosion = cv2.erode(img,kernel,iterations=1)
dilation = cv2.dilate(img,kernel,iterations=1)
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
blackhat = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)

cv2.namedWindow('Original',cv2.WINDOW_KEEPRATIO)
cv2.namedWindow('morphologyEX',cv2.WINDOW_KEEPRATIO)

cv2.imshow('Original',img)
# cv2.imshow('morphologyEX',erosion)
# cv2.imshow('morphologyEX',dilation)
# cv2.imshow('morphologyEX',opening)
# cv2.imshow('morphologyEX',closing)
# cv2.imshow('morphologyEX',gradient)
# cv2.imshow('morphologyEX',tophat)
cv2.imshow('morphologyEX',blackhat)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
