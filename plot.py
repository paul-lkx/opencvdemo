
import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img, (0,0), (511,511), (255,0,0), 5, cv2.LINE_AA)

cv2.rectangle(img, (384,0), (510,128), (0,255,0), 3)

cv2.circle(img, (447,63), 63, (0,0,255), -1)

cv2.ellipse(img, (256,256), (100,50), 0, 0, 180, 255, -1)

pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, pts, 1, color=(255,255,255))

font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
cv2.putText(img, 'Hi, Dailong!', (10,500), font, 2, (255,255,255))
cv2.imshow('plot', img)
k = cv2.waitKey(0)
if k == 27:              # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):      # wait for 's' key to save and exit
    cv2.imwrite('Chris1.png', img)
    cv2.destroyAllWindows()