import cv2

img=cv2.imread("Resources/default.png")

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny=cv2.Canny(img,100,100)


cv2.imshow("Gray image", imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Blur Image",imgCanny)
cv2.waitKey(0)