#color detection
import cv2
import numpy as np
path="../Resources/lambo.png"
img=cv2.imread(path)
imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
hor=np.hstack((img,imgHSV))
cv2.imshow("2 images: ",hor)
cv2.waitKey(0)