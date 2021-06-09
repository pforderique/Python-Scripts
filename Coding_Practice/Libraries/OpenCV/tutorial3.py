'''
Tutorial 3: Cameras and VideoCapture

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

    #? what if I want to have a quadrant of my faces?
    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)

    image[:height//2, :width//2] = cv2.flip(smaller_frame, 1) # mirror horizontally
    image[height//2:, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    image[:height//2, width//2:] = np.expand_dims(cv2.cvtColor(smaller_frame, cv2.COLOR_BGR2GRAY), axis=2)
    image[height//2:, width//2:] = smaller_frame


    cv2.imshow('frame', image)

    #* quit if you press q within 1 millisecond
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()