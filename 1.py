#!/bin/lib/python

import cv2
import numpy as np

img = cv2.imread('j1.jpg',0)
kernel = np.ones((5,5),np.uint8)

erosion = cv2.erode(img,kernel,iterations=1)
dilation = cv2.dilate(img,kernel,iterations=1)
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)

cv2.namedWindow('Original',cv2.WINDOW_KEEPRATIO)
cv2.namedWindow('morphologyTransformation',cv2.WINDOW_KEEPRATIO)

cv2.imshow('Original',img)
# cv2.imshow('morphologyTransformation',erosion)
# cv2.imshow('morphologyTransformation',dilation)
# cv2.imshow('morphologyTransformation',opening)
cv2.imshow('morphologyTransformation',closing)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
