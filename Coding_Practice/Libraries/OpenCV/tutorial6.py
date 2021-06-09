'''
Tutorial 6: Corner Detection - Shi-Tomasi Algorithm

Piero Orderique
09 June 2021
'''

import numpy as np
import cv2

img = cv2.imread('Detection/assets/cover.jpg')

#* Easier to detect edges in black in white
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#* run the algorithm
# get the 5 best corners, 0.2 degree of confidence, minimum ecluidian distance of 1
corners = cv2.goodFeaturesToTrack(gray, 150, 0.01, 1) 
corners = np.int0(corners)

#* draw a circle at each corner
for corner in corners:
    x, y = corner.ravel() # ravel takes [[[1, 2, 3]]] -> [1,2,3]
    cv2.circle(img, (x,y), 5, (255,0,0), -1) # if negative, it FILLS the shape
    print(x,y)

# fun with lines
for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        c1 = tuple(corners[i][0])
        c2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, c1, c2, color, 1)

cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()