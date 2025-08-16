import numpy as np
import cv2 as cv
cap=cv.VideoCapture('./obs/americanf.mp4')

def processing(frame):
    ans=cv.resize(frame,(700,700))
    ans=cv.Canny(ans,100,100)
    return ans


while cap.isOpened():
    ret, frame=cap.read()
    ans=processing(frame)
    cv.imshow('video ',ans)
    if cv.waitKey(1)==ord('q'):
        break

cap.release()
cv.destroyAllWindows()