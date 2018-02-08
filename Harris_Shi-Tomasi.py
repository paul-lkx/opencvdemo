#!/bin/lib/python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

filename = 'c2.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

# # img - 数据类型为 float32 的输入图像。
# # blockSize - 角点检测中要考虑的领域大小。
# # ksize - Sobel 求导中使用的窗口大小
# # k - Harris 角点检测方程中的自由参数,取值参数为 [0,04,0.06].
# dst = cv2.cornerHarris(gray,2,3,0.04)
#
# # result is dilated for making the corners, not important
# dst = cv2.dilate(dst,None)
#
# # Threshold for an optimal value, it may vary depending on the image
# img[dst > 0.01*dst.max()] = [0,0,255]


# Shi-Tomasi 焦点检测
corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
# 返回的结果是 [[ 311., 250.]] 两层括号的数组。
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()