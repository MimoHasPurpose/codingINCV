# task did image blending of 2 images.

import cv2 as cv
import numpy as np
img1 = cv.imread('./obs/dog_studying.jpg')
img2 = cv.imread('./obs/mmeme.jpg')
def imblend(img1,img2):
    
    dst = cv.addWeighted(img1,0.7,img2,0.3,0)
    cv.imshow('dst',dst)
    cv.waitKey(0)
    cv.destroyAllWindows()


img1=img1[0:500,0:500]
img2=img2[0:500,0:500]
print(img1.shape, img2.shape)

imblend(img1,img2)
imblend(img1,img1)