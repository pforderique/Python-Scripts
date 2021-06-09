'''
Tutorial 4: Drawing lines, images, circles, text on a frame

Piero Orderique
09 June 2021
'''

import numpy as np
import cv2

#* load video capture
cap = cv2.VideoCapture(0) # select the webcam OR path to a video

while True:
    #* get a frame from out video capture device
    ret, frame = cap.read() # ret tells us if its busy or not
    width = int(cap.get(3)) # 3 is the identifier for width property
    height = int(cap.get(4))

    #* draw a line 
    img = cv2.line(frame, (0,0), (width, height), (255,0,0), 10)
    img = cv2.line(img, (0,height), (width, 0), (0,255,0), 10)

    #* draw rect
    img = cv2.rectangle(img, (100,100), (200,200), (128,128,128), -1) # if negative, it FILLS the shape

    #* draw rect
    img = cv2.circle(img, (width//2,height//2), 30, (0,0,255), 10) # if negative, it FILLS the shape

    #* draw text
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Im Piero!', (200,height - 10), font, 2, (0,0,0), 5, cv2.LINE_AA) # put in coordinates of bottom left hand corner  

    cv2.imshow('frame', frame)

    #* quit if you press q within 1 millisecond
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()