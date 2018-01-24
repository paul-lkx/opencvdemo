#!/bin/lib/python

import cv2
import numpy as np

# load the images
img1 = cv2.imread('c1.jpg')
img2 = cv2.imread('c2.jpg')

# I want to put logo on the top-left corner,So I create a ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 175, 225, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
# print(img1_bg,mask_inv)

# Take the only region og logo from logo image
img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)


dst = cv2.add(img1_bg, img2_fg)

img1[0:rows, 0:cols] = dst


# print img1.shape, img2.shape

cv2.namedWindow('res',cv2.WINDOW_KEEPRATIO)
cv2.imshow('res',img1)
k = cv2.waitKey(0)
if k == 27:              # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):      # wait for 's' key to save and exit
    cv2.imwrite('add.png', img2)
    cv2.destroyAllWindows()