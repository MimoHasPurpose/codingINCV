import cv2
import numpy as np
image=cv2.imread("../Resources/default.png")
print(image.shape)
#widthxheight
imgResize=cv2.resize(image,(400,400))
print(imgResize.shape)
#widhtxheight
imgCropped=image[0:200,200:500]
cv2.imshow("cropped",imgCropped)
cv2.imshow("Image",image)
cv2.imshow("Resized",imgResize)
cv2.waitKey(0)