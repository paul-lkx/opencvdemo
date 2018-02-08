#!/bin/lib/python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

filename = 'natlight_evemorn-ex1.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


sift = cv2.SIFT()
kp = sift.detect(gray,None)
img = cv2.drawKeypoints(gray,kp)

# img = cv2.drawKeypoints(gray,kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()