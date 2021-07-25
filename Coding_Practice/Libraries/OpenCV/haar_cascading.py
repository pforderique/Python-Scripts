# HAAR CASCASE METHOD:
# feature based machine learning 

# uses pretrained images of labeled poitives and negatives
# runs through thousands of classifiers in a cascaded manner
# Use cases: detecting faces

import numpy as np
import cv2

img = cv2.imread("Detection/assets/faces.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
path = 'Detection/haarcascade_frontalface_default.xml'
path = 'Detection/haarcascade_eye.xml'

face_cascade = cv2.CascadeClassifier(path)

faces= face_cascade.detectMultiScale(
    gray, scaleFactor=1.02, minNeighbors=20, minSize=(10,10))
print(f'Num of faces: {len(faces)}')

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()