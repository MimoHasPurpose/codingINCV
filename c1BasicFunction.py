import cv2
import numpy as np
img=cv2.imread("Resources/default.png")
kernel=np.ones((5,5),np.unit8)
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny=cv2.Canny(img,100,100)
imgDialation=cv2.dilate(imgCanny,)

cv2.imshow("Gray image", imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Blur Image",imgCanny)
cv2.waitKey(0)