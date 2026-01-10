import cv2
print("Package imported")
img=cv2.imread("../Resources/1.jpg")

cv2.imshow("Output",img)
#0 means infinte delay, 1000 means i second
cv2.waitKey(0)