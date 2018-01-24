

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load an color image in grayscale
img = cv2.imread('c1.jpg')
img1 = cv2.imread('Chris1.png')
# print(img.shape,img1.shape)
dst = cv2.addWeighted(img,0.7,img1,0.3,0)
# print(img.shape,img1.shape)
# chris = img[:,550:1550]
# img[:,0:1000] = chris
# b,g,r = cv2.split(img)
# # img[:,:,2] = 0
# img[:,1000:] = chris[:,0:920]

# BLUE = [255,0,0]
#
# replicate = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)
# reflect = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)
# reflect101 = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT_101)
# wrap = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP)
# constant = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
#
# plt.subplot(231).imshow(img,'gray'),plt.title('ORIGINAL')
# plt.subplot(232).imshow(replicate,'gray'),plt.title('REPLICATE')
# plt.subplot(233).imshow(reflect,'gray'),plt.title('REFLECT')
# plt.subplot(234).imshow(reflect101,'gray'),plt.title('REFLECT_101')
# plt.subplot(235).imshow(wrap,'gray'),plt.title('WRAP')
# plt.subplot(236).imshow(constant,'gray'),plt.title('CONSTANT')
#
# plt.show()


cv2.namedWindow('footballstar',cv2.WINDOW_KEEPRATIO)
cv2.imshow('footballstar',dst)


k = cv2.waitKey(0)
if k == 27:              # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):      # wait for 's' key to save and exit
    cv2.imwrite('Chris1.png', dst)
    cv2.destroyAllWindows()
#
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.xticks([]), plt.yticks([])
# plt.show()