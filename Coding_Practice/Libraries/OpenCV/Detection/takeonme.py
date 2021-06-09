'''
Attempt to create a "take on me" filter
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

    #* There's RGB, BGR, and HSV - Hue, Saturation, and Bright/Lightness
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #* extract colors -- choose lower and upperborund -- use an hsv color picker for better range!
    # lower = np.array([0, 0, 50])
    # upper = np.array([10, 150, 255])
    lower = np.array([0, 50, 50])
    upper = np.array([10, 190, 235])
    mask = cv2.inRange(hsv, lower, upper)

    #* apply the mask -- compate bits form the mask to the bits in our frame
    result = cv2.bitwise_and(frame, frame, mask=mask) # 1 1 = 1 // 0 1 = 0 // 0 0 = 1 // 0 1 = 0

    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)

    #* quit if you press q within 1 millisecond
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()