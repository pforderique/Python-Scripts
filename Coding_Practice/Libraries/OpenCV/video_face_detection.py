import numpy as np
import cv2

cap = cv2.VideoCapture(2)
path = 'Detection/haarcascade_frontalface_default.xml'

color = (0,255,0)
line_width = 3
radius = 3
point = (0,0)

def click(event, x, y, flags, param):
    global point, pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Pressed {x}, {y}")
        point = (x,y)

# set the click callback!
cv2.namedWindow("video")
cv2.setMouseCallback("video", click)

while True:
    ret, frame = cap.read()

    # frame = cv2.resize(frame, (0,0), fx=2, fy=2)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(path)
    faces= face_cascade.detectMultiScale(
        gray, scaleFactor=1.02, minNeighbors=10, minSize=(40,40))

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

    # cv2.circle(frame, point, radius, color, line_width)
    cv2.imshow("video", frame)

    ch = cv2.waitKey(1) 
    if ch & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()