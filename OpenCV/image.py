



import cv2 as cv
import numpy as np


def resizee(img):
    res = cv.resize(img,None,fx=0.5, fy=0.5, interpolation = cv.INTER_CUBIC)
    cv.imshow("image resized: ", res)



img=cv.imread("..//Resources//ghibili.jpg")
# print(img,img.shape)
# cv.imshow("Output",img)
# kernel = np.ones((5,5),np.float32)/25
# dst = cv.filter2D(img,-1,kernel)
# cv.imshow("smoothening", dst)
#0 means infinte delay, 1000 means i second


resizee(img)
cv.waitKey(0)
