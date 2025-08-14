# performance measurement and improv techniques.
# https://scipy-lectures.org/advanced/advanced_numpy/index.html#advanced-numpy
import cv2 as cv
import numpy as np

e1 = cv.getTickCount()


img1 = cv.imread('./obs/dog_studying.jpg')
img2 = cv.imread('./obs/mmeme.jpg')
def imblend(img1,img2):
    
    dst = cv.addWeighted(img1,0.7,img2,0.3,0)
    cv.imshow('dst',dst)
    cv.waitKey(0)
    cv.destroyAllWindows()


img1=img1[0:500,0:500]
img2=img2[0:500,0:500]


imblend(img1,img2)



e2 = cv.getTickCount()
time = (e2 - e1)/ cv.getTickFrequency()
print(time)