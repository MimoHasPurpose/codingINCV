#viola and  and jones method for  object detection
#positive and negative  non faces train and make a cascade xml file.
# open cv has default cascades
import cv2
imagePath='../Resources/lena.png'
img=cv2.imread(imagePath)
#convert the image to grayscale
gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
face=face_classifier.detectMultiScale(gray_image,scaleFactor=1.1,minNeighbors=5,minSize=(40,40))

for(x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow("face detected",img_rgb)
cv2.waitKey(0)