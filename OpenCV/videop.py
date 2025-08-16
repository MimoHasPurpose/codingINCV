import numpy as np
import cv2 as cv
print("hi")
cap = cv.VideoCapture('./obs/2face.mp4')

while cap.isOpened():
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    gray_s=cv.resize(gray,(700,800))

    cv.imshow('frame', gray_s)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()